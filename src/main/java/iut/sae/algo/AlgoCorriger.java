package iut.sae.algo;

public class AlgoCorriger {

    public static String RLE(String in){
        String newChaine= "";
        int cpt = 1 ;  // On initialise le compteur à 1 
        for(int i=0;i<in.length(); i++){ // On parcourt la chaine 
            if(i < in.length()-1 && in.charAt(i)==in.charAt(i+1) && cpt<9){ //Si ce n'est pas le dernier caractere de la chaine et que le caractere suivant est pareil et que le compteur est inferieur à 9  
                cpt ++;                       // Alors on incrémente le compteur
            }
            else{ // Sinon on ajoute le compteur + le caractere dans la chaine a retourner 
                newChaine = newChaine + cpt + in.charAt(i);
                cpt = 1; // Et on remet le compteur à 1
            }

        }
        return newChaine;
    }

    public static String RLE(String in, int iteration) {
        if(iteration !=1){   // Tant que l'iteration n'est pas 1 on continue a faire tourner le programme 
            String nouvelchaine = RLE(in);
            return RLE(nouvelchaine,iteration-1); //On decremente a chaque fois l'iteration jusqua arriver à 1 
        }
        return RLE(in); // Ducoup si iteration == 1 c'est un RLE simple et c'est le résultat final 
    }

    public static String unRLE(String in) {
        String newChaine= "";
        for(int i=0;i<in.length(); i=i+2){ // Boucle avec un pas de 2 car on n'a pas besoin de parcourir les "caractères" 
            for(int y=0;y<Character.getNumericValue(in.charAt(i)) ;y++){ //Boucle pour construire le nombre de caractere dans la nouvelle chaine
                newChaine = newChaine + in.charAt(i+1);
            }
            
        }
        return newChaine;
    }

    public static String unRLE(String in, int iteration){
        if(iteration !=1){                      //J'ai repris mon algo RLE recursif en changeant la methode en unRLE 
            String nouvelchaine = unRLE(in);
            return unRLE(nouvelchaine,iteration-1); 
        }
        return unRLE(in); 
    }
}