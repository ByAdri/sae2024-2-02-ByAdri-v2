package iut.sae.algo;

public class Algo {

    public static String RLE(String in) {
        if (in == null || in.isEmpty()) {
            return "";
        }

        StringBuilder sb = new StringBuilder();
        int length = in.length();
        int count = 1;
        char currentChar = in.charAt(0);

        for (int i = 1; i < length; i++) {
            if (in.charAt(i) == currentChar) {
                count++;
            } else {
                appendRLE(sb, count, currentChar);
                currentChar = in.charAt(i);
                count = 1;
            }
        }

        // Append the last sequence
        appendRLE(sb, count, currentChar);

        return sb.toString();
    }

    private static void appendRLE(StringBuilder sb, int count, char c) {
        if (count > 9) {
            // If count is more than 9, handle it efficiently
            sb.append(9).append(c).append(count - 9).append(c);
        } else {
            // Otherwise, append normally
            sb.append(count).append(c);
        }
    }

    public static String RLE(String in, int iteration) throws AlgoException {
        if (iteration < 1) {
            throw new AlgoException("Iteration count must be at least 1");
        }

        String result = in;
        for (int i = 0; i < iteration; i++) {
            result = RLE(result);  // Recursive call to the base RLE method
        }

        return result;
    }

    public static String unRLE(String in) throws AlgoException {
        if (in == null || in.isEmpty()) {
            return "";
        }

        StringBuilder sb = new StringBuilder();
        int length = in.length();
        int count = 0;

        for (int i = 0; i < length; i++) {
            char c = in.charAt(i);
            if (Character.isDigit(c)) {
                count = count * 10 + (c - '0');
            } else {
                if (count == 0) {
                    throw new AlgoException("Invalid input format");
                }
                sb.append(String.valueOf(c).repeat(count));
                count = 0;
            }
        }

        return sb.toString();
    }

    public static String unRLE(String in, int iteration) throws AlgoException {
        if (iteration < 1) {
            throw new AlgoException("Iteration count must be at least 1");
        }

        String result = in;
        for (int i = 0; i < iteration; i++) {
            result = unRLE(result);  // Recursive call to the base unRLE method
        }

        return result;
    }
}
