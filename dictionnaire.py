mon_dictionnaire = {}
continuer = "o"

def mon_dico():

    while continuer == "o":
        # name = input("Entrez une catégorie de produit : ")
        
        categorie = input("Entrez une catégorie de produit : ")

        if categorie in mon_dictionnaire:

            print(mon_dictionnaire[categorie])

            print(" Cette catégories existe déjà voulez-vous : \n1: Supprimez un élément existant\n2: Ajouter un élément\n3: Vider les stock")
            action = input("\n >: ")
            match action:
                case "1":
                   v = input("Entrez une valeur à supprimer : ")
                   mon_dictionnaire.remove(v)
                
                case "2":
                   a  = input("Entrez une valeur à ajouter : ")
                   mon_dictionnaire.append(a)

                case "3":
                     oui = mon_dictionnaire.clear()
                     vider = input("Voulez-vous vraiment vider ? : ", oui)
                     mon_dictionnaire.clear()
                     pass
            print(f"Le dictionnaire est maintenant : {mon_dictionnaire}")

        else:
            valeur = input("Entrez une valeur pour cette catégorie : ")
            mon_dictionnaire[categorie] = [valeur]
            print(f"Le dictionnaire est maintenant : {mon_dictionnaire}")


mon_dico()

