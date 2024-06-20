import unittest

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


class TestAlgoCorriger(unittest.TestCase):
    def test_RLE(self):
        self.assertEqual("", simplicite.RLE(""))
        self.assertEqual("1a1b1c", simplicite.RLE("abc"))
        self.assertEqual("1a2b3c", simplicite.RLE("abbccc"))
        self.assertEqual("3a1b2a", simplicite.RLE("aaabaa"))
        self.assertEqual("1a1A1a", simplicite.RLE("aAa"))
        self.assertEqual("9W4W", simplicite.RLE("WWWWWWWWWWWWW"))

        # Supplementary tests
        self.assertEqual("1a1b1c1A1B1C1D1E1d1e", simplicite.RLE("abcABCDEde"))
        self.assertEqual("1a1b9B7B2b1c", simplicite.RLE("abBBBBBBBBBBBBBBBBbbc"))
        self.assertEqual("2a", simplicite.RLE("aa"))
        self.assertEqual("111213", simplicite.RLE("123"))
        self.assertEqual("259n9n2n3z2r1t1r1y261019", simplicite.RLE("55nnnnnnnnnnnnnnnnnnnnzzzrrtry6609"))

    def test_RLE_recursif(self):
        try:
            self.assertEqual("", simplicite.RLE_iterations("", 1))
            self.assertEqual("", simplicite.RLE_iterations("", 3))

            self.assertEqual("1a1b1c", simplicite.RLE_iterations("abc", 1))
            self.assertEqual("1a2b3c", simplicite.RLE_iterations("abbccc", 1))
            self.assertEqual("3a1b2a", simplicite.RLE_iterations("aaabaa", 1))
            self.assertEqual("1a1A1a", simplicite.RLE_iterations("aAa", 1))

            self.assertEqual("111a111b111c", simplicite.RLE_iterations("abc", 2))
            self.assertEqual("311a311b311c", simplicite.RLE_iterations("abc", 3))

            sae_ite20 = "1113122113121113222123211211131211121311121321123113213221121113122123211211131221121311121312211213211321322112311311222113311213212322211211131221131211221321123113213221121113122113121113222112131112131221121321131211132221121321132132211331121321232221123113112221131112311322311211131122211213211331121321122112133221121113122113121113222123112221221321132132211231131122211331121321232221121113122113121113222123113221231231121113213221231221132221222112112322211S1113122113121113222123211211131211121311121321123113213221121113122123211211131221121311121312211213211321322112311311222113311213212322211211131221131211221321123113213221121113122113121113222112131112131221121321131211132221121321132132211331121321232221123113112221131112311322311211131122211213211331121321122112133221121113122113121113222123112221221321132132211231131122211331121321232221121113122113121113222123113221231231121113213221231221132221222112112322211A1113122113121113222123211211131211121311121321123113213221121113122123211211131221121311121312211213211321322112311311222113311213212322211211131221131211221321123113213221121113122113121113222112131112131221121321131211132221121321132132211331121321232221123113112221131112311322311211131122211213211331121321122112133221121113122113121113222123112221221321132132211231131122211331121321232221121113122113121113222123113221231231121113213221231221132221222112112322211E1113122113121113222123211211131211121311121321123113213221121113122123211211131221121311121312211213211321322112311311222113311213212322211211131221131211221321123113213221121113122113121113222112131112131221121321131211132221121321132132211331121321232221123113112221131112311322311211131122211213211331121321122112133221121113122113121113222123112221221321132132211231131122211331121321232221121113122113121113222123113221231231121113213221231221132221222112112322211 1113122113121113222123211211131211121311121321123113213221121113122123211211131221121311121312211213211321322112311311222113311213212322211211131221131211221321123113213221121113122113121113222112131112131221121321131211132221121321132132211331121321232221123113112221131112311322311211131122211213211331121321122112133221121113122113121113222123112221221321132132211231131122211331121321232221121113122113121113222123113221231231121113213221231221132221222112112322211A1113122113121113222123211211131211121311121321123113213221121113122123211211131221121311121312211213211321322112311311222113311213212322211211131221131211221321123113213221121113122113121113222112131112131221121321131211132221121321132132211331121321232221123113112221131112311322311211131122211213211331121321122112133221121113122113121113222123112221221321132132211231131122211331121321232221121113122113121113222123113221231231121113213221231221132221222112112322211l1113122113121113222123211211131211121311121321123113213221121113122123211211131221121311121312211213211321322112311311222113311213212322211211131221131211221321123113213221121113122113121113222112131112131221121321131211132221121321132132211331121321232221123113112221131112311322311211131122211213211331121321122112133221121113122113121113222123112221221321132132211231131122211331121321232221121113122113121113222123113221231231121113213221231221132221222112112322211g1113122113121113222123211211131211121311121321123113213221121113122123211211131221121311121312211213211321322112311311222113311213212322211211131221131211221321123113213221121113122113121113222112131112131221121321131211132221121321132132211331121321232221123113112221131112311322311211131122211213211331121321122112133221121113122113121113222123112221221321132132211231131122211331121321232221121113122113121113222123113221231231121113213221231221132221222112112322211o"
            self.assertEqual(sae_ite20, simplicite.RLE_iterations("SAE Algo", 20))

            sae_ite15 = "311311222113111231133211121312211231131112311211133112111312211213211312111322211231131122111213122112311311221132211221121332211a311311222113111231133211121312211231131112311211133112111312211213211312111322211231131122111213122112311311221132211221121332211z311311222113111231133211121312211231131112311211133112111312211213211312111322211231131122111213122112311311221132211221121332211e311311222113111231133211121312211231131112311211133112111312211213211312111322211231131122111213122112311311221132211221121332211r311311222113111231133211121312211231131112311211133112111312211213211312111322211231131122111213122112311311221132211221121332211t311311222113111231133211121312211231131112311211133112111312211213211312111322211231131122111213122112311311221132211221121332211y"
            self.assertEqual(sae_ite15, simplicite.RLE_iterations("azerty", 15))
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

    def test_unRLE(self):
        try:
            self.assertEqual("", simplicite.unRLE(""))
            self.assertEqual("abc", simplicite.unRLE("1a1b1c"))
            self.assertEqual("abbccc", simplicite.unRLE("1a2b3c"))
            self.assertEqual("aaabaa", simplicite.unRLE("3a1b2a"))
            self.assertEqual("aAa", simplicite.unRLE("1a1A1a"))
            self.assertEqual("WWWWWWWWWWWWW", simplicite.unRLE("9W4W"))

            # Supplementary tests
            self.assertEqual("aaAAaaBBaa", simplicite.unRLE("2a2A2a2B2a"))
            self.assertEqual("aAAbbbBBBBccccc", simplicite.unRLE("1a2A3b4B5c"))
            self.assertEqual("aAAbbbBBBBccccc", simplicite.unRLE(simplicite.RLE("aAAbbbBBBBccccc")))
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

    def test_unRLE_recursif(self):
        try:
            self.assertEqual("", simplicite.unRLE_iterations("", 1))
            self.assertEqual("", simplicite.unRLE_iterations("", 3))

            self.assertEqual("abc", simplicite.unRLE_iterations("1a1b1c", 1))
            self.assertEqual("abbccc", simplicite.unRLE_iterations("1a2b3c", 1))
            self.assertEqual("aaabaa", simplicite.unRLE_iterations("3a1b2a", 1))
            self.assertEqual("aAa", simplicite.unRLE_iterations("1a1A1a", 1))

            self.assertEqual("abc", simplicite.unRLE_iterations("111a111b111c", 2))
            self.assertEqual("abc", simplicite.unRLE_iterations("311a311b311c", 3))

            # Supplementary tests
            self.assertEqual("aaaavrrvr", simplicite.unRLE_iterations("3114311a13211v3112311r13211v13211r", 4))
            self.assertEqual("zzzzERRTTTRZaz", simplicite.unRLE_iterations(
                "1113122114111312211z31131122211E1113122112111312211R11131211121312211T31131122211R31131122211Z31131122211a31131122211z",
                6))
            self.assertEqual("azerty", simplicite.unRLE_iterations(simplicite.RLE_iterations("azerty", 15), 15))
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")


if __name__ == '__main__':
    unittest.main()
