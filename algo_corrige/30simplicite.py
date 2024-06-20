"""
Algoritme de compression de chaîne 
"""
def RLE(chaine : str) :
    #Initialisation d'une chaine et d'un indice
    chaineCompress = ""
    i = 0

    while i < len(chaine) :
        #Compteur à 1 pour le caractère courant
        cptChar = 1

        #Tant que le suivant est égale au courant et qu'il existe dans la chaine, et que le compteur ne dépasse pas 9...
        while i+cptChar < len(chaine) and chaine[i] == chaine[i+cptChar] and cptChar < 9:
            #...on incrémente le compteur 
            cptChar += 1

        #On ajoute à la chaine compressée le compteur et le caractère
        chaineCompress += str(cptChar) + chaine[i]
        #On passe au prochain caractère différent
        i += cptChar

    return chaineCompress

def RLE_rec(chaine : str, iteration : int) :
    if iteration == 0 :
        return chaine
    else :
        return RLE_rec(RLE(chaine), iteration-1)
    

def unRLE(chaine : str) :
    #Initialisation d'une chaine
    chaineDecompress = ""

    #On parcourt la chaine de 2 en 2 (pour chaque couple compteur/caractère)
    for i in range(0, len(chaine), 2) :
        #On récupère le compteur devant le caractère...
        cptChar = int(chaine[i])
        #... et on ajoute le caractère le nombre de fois nécessaire (=compteur)
        chaineDecompress += chaine[i+1]*cptChar
    
    return chaineDecompress


def unRLE_rec(chaine : str, iteration : int) :
    if iteration == 0 or chaine[0] not in ["0","1","2","3","4","5","6","7","8","9"] :
        return chaine
    else :
        return unRLE_rec(unRLE(chaine), iteration-1)