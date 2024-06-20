package iut.sae.algo;

public class simplicite23 {

    public static void main(String[] args) {
        String chaine="wwwwwwwwwwwwwwwwttowwwwwwoooo"; // Ajoutez la chaîne que vous souhaitez compresser ici
        String Compressed = classicCompress(chaine); // Appel à la méthode de compression
        System.out.println("Chaîne après compression : " + Compressed); // Affiche la chaîne compressée
        System.out.println("Décompression : " + classicUnCompress(Compressed)); // Affiche la chaîne après décompression
    }

    // Méthode pour compresser une chaîne en utilisant un algorithme simple de compression par comptage
    public static String classicCompress(String chaine) {
        String Compressed = "";
        char current = chaine.charAt(0); // Premier caractère de la chaîne
        int nbcurrent = 1; // Compteur du nombre de fois où le caractère actuel se répète
        for (int i = 1; i < chaine.length(); i++) {
            if (chaine.charAt(i) == current) {
                if(nbcurrent>=9){
                    Compressed += Character.toString(current); // Ajoute le caractère compressé
                    Compressed += Integer.toString(nbcurrent); // Ajoute le compteur de répétitions
                    nbcurrent=1;
                }
                nbcurrent++; // Incrémente le compteur si le caractère est le même que le précédent
            } else {
                Compressed += Character.toString(current); // Ajoute le caractère compressé
                Compressed += Integer.toString(nbcurrent); // Ajoute le compteur de répétitions
                current = chaine.charAt(i); // Met à jour le caractère actuel
                nbcurrent = 1; // Réinitialise le compteur
            }
        }
        // Ajoute le dernier caractère compressé et son compteur
        Compressed += Character.toString(current);
        Compressed += Integer.toString(nbcurrent);
        return Compressed; // Retourne la chaîne compressée
    }

    // Méthode pour décompresser une chaîne compressée
    public static String classicUnCompress(String chaine) {
        String unCompressed = "";
        char current;
        int nbcurrent;
        for (int i = 0; i < chaine.length(); i++) {
            current = chaine.charAt(i); // Lit le caractère
            i++;
            nbcurrent = Character.getNumericValue(chaine.charAt(i)); // Lit le compteur de répétitions
            for (int j = 0; j < nbcurrent; j++) {
                unCompressed += current; // Ajoute le caractère le nombre de fois spécifié
            }
        }
        return unCompressed; // Retourne la chaîne décompressée
    }
    
}

