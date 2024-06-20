package iut.sae.algo;

public class Efficacite {
    public static String RLE(String in) {
        char previous;
        if (in.length() != 0)
            previous = in.charAt(0);
        else
            return "";
        StringBuilder result = new StringBuilder();
        int iteration = 0;
        for (char c : in.toCharArray()) {
            if (c == previous && iteration < 9) {
                iteration += 1;
            } else {
                result.append(iteration).append(previous);
                iteration = 1;
                previous = c;
            }
        }
        result.append(iteration).append(previous);
        return result.toString();
    }

    public static String RLE(String in, int iteration) throws AlgoException {
        while (iteration > 0) {
            in = RLE(in);
            iteration--;
        }
        return in;
    }

    public static String unRLE(String in) throws AlgoException {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < in.length(); i += 2) {
            int count = Character.getNumericValue(in.charAt(i));
            for (int j = 0; j < count; j++) {
                result.append(in.charAt(i + 1));
            }
        }
        return result.toString();
    }

    public static String unRLE(String in, int iteration) throws AlgoException {
        while (iteration > 0) {
            in = unRLE(in);
            iteration--;
        }
        return in;
    }
}
