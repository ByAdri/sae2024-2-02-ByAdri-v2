def RLE(chaine):
    result = ""  # Chaine résultat
    nbChar = 1  # Nombre de caractères de répétition
    i = 0  # Compteur
    while i < len(chaine):  # Parcours de la chaine
        while i < len(chaine) - 1 and chaine[i] == chaine[i + 1] and nbChar < 9:  # Boucle répétition de caractères
            nbChar += 1
            i += 1
        result += chaine[i] + str(nbChar)  # Ajouter résultat boucle répétition au résultat
        i += 1
        nbChar = 1  # Réinitialisation du nombre de caractères


def RLE_recursive(chaine, i=0, nbChar=1, result=""):
    if i >= len(chaine):
        return result
    if i < len(chaine) - 1 and chaine[i] == chaine[i + 1] and nbChar < 9:
        return RLE_recursive(chaine, i + 1, nbChar + 1, result)
    else:
        result += chaine[i] + str(nbChar)
        return RLE_recursive(chaine, i + 1, 1, result)

def unRLE(chaine):
    result = ""  # Chaine résultat
    i = 0  # Compteur
    while i < len(chaine):  # Parcours de la chaine compressée
        char = chaine[i]  # Caractère
        nbChar = int(chaine[i + 1])  # Nombre de répétitions
        result += char * nbChar  # Ajouter les répétitions du caractère au résultat
        i += 2  # Passer au prochain caractère compressé
    return result


def unRLE_recursive(chaine, i=0, result=""):
    if i >= len(chaine):
        return result
    char = chaine[i]
    nbChar = int(chaine[i + 1])
    result += char * nbChar
    return unRLE_recursive(chaine, i + 2, result)