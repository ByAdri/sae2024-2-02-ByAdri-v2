package iut.sae.algo;


public class Algo{

    public static String RLE(String source) {

        String chaineCodee = "";
    
        for (int i = 0; i < source.length(); i++) {
            int nbCaracteres = 1;
    
            while (i + 1 < source.length() && source.charAt(i) == source.charAt(i + 1)) {

                nbCaracteres++;
                i++;
    
                if (nbCaracteres == 9) {
                    chaineCodee += "9" + source.charAt(i);
                    nbCaracteres = 0;
                }
            }
    
            chaineCodee += "" + nbCaracteres + source.charAt(i);
            
        }
    
        return chaineCodee;
    }
    
        

    public static String RLE(String source, int iteration) throws AlgoException{
        if (iteration < 1) {
            throw new AlgoException("L'itération doit être >= 1");
        }
        
        for (int i = 0; i < iteration; i++) {
            source = RLE(source);
        }
        return source;
    }


    public static String unRLE(String source) throws AlgoException{
      
        String chaineDecodee = "";

        for (int i = 0; i < source.length(); i++) {
            
            char nbCaracteres = source.charAt(i);
            //convertit le charactere récupéré en int
            int nbLettres = nbCaracteres - '0';
            char lettre = source.charAt(i + 1);
            

            for (int j = 0; j < nbLettres; j++) {
                chaineDecodee += lettre;
            }

            i++;
        }

        return chaineDecodee;

    }

    public static String unRLE(String source, int iteration) throws AlgoException{
        
        if (iteration < 1) {
            throw new AlgoException("L'itération doit être >= 1");
        }
        
        for (int i = 0; i < iteration; i++) {
            source = unRLE(source);
        }
        return source;

    }
}

