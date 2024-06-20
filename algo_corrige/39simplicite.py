class simplicite:
    def RLE(texte):
        #vérifier que le texte en entrée n'est pas vide
        if texte is None or len(texte) == 0:
            return ""
        
        #création des variables
        sortie = ""
        char_precedent = texte[0]
        nombre_repetitions = 1

        #boucle pour parcourir le texte
        for i in range(1, len(texte)):
            #vérifier que le caractère actuel est le même que le précédent
            if texte[i] == char_precedent:
                #vérifier que le nombre de repetitions d'un caractère ne dépasse pas 9
                if nombre_repetitions > 8:
                    #construction du message de sortie en cas de dépassement de la limite
                    
                    #concaténer le nombre de répétitions en string avec le caractère répété
                    sortie += str(nombre_repetitions) + char_precedent
                    #attribution de la valeur du texte actuel à la variable du caractère précédent
                    char_precedent = texte[i]
                    #reinitialisation de la variable du nombre de répétitions à 1
                    nombre_repetitions = 1
                else:
                    #si la limite n'est pas atteinte on ajoute une répétition à la lettre actuelle
                    nombre_repetitions += 1
            else:
                #en cas de changement de lettre
                sortie += str(nombre_repetitions) + char_precedent
                char_precedent = texte[i]
                nombre_repetitions = 1

        #Ajout du dernier caractères et son nombre de répétitions
        sortie += str(nombre_repetitions) + char_precedent
        return sortie

    def RLE_iterations(texte, iteration):
        #attribution de la valeur du texte actuel à la variable de sortie
        sortie = texte

        #boucle pour répéter la fonction RLE "iteration" fois
        for i in range(iteration):
            sortie = simplicite.RLE(sortie)

        return sortie

    def unRLE(texte):
        #vérifier que le texte en entrée n'est pas vide
        if texte is None or len(texte) == 0:
            return ""

        #création de la variable à return
        sortie = ""

        #vérifier que le premier caractère du texte est un chiffre
        if not texte[0].isdigit():
            return texte

        #boucle pour parcourir le texte
        for i in range(1, len(texte), 2):
            #récupération du nombre de répétition des caractères à décompresser
            nombre_repetitions = int(texte[i - 1])
            #attribution de la valeur du texte actuel à la variable du caractère précédent
            char_precedent = texte[i]

            for j in range(nombre_repetitions):
                #concaténer la valeur de sortie avec le caractère répété
                sortie += char_precedent

        return sortie

    def unRLE_iterations(texte, iteration):
        #attribution de la valeur du texte actuel à la variable de sortie
        sortie = texte

        #boucle pour répéter la fonction RLE "iteration" fois
        for i in range(iteration):
            sortie = simplicite.unRLE(sortie)
        return sortie