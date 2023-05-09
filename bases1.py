import sqlite3

conn = sqlite3.connect("./moko.db")

cur = conn.cursor()



# choisi une option
user_entrer = int(input("""
    Choisissez parmis les 5 options suivant:
    1 - Lister tous les élèves 
    2 - Ajouter un élève
    3 - Modifier un élève
    4 - Supprimer un élève  
    ? Votre choix : >_ """
))

if user_entrer == 1:
    # Lister tous les élèves
    print(cur)

elif user_entrer == 2:
    def ajoute(nom,age,classe):
        nom = input("Entrer le nom de l'élève : ")
        age = input("Entrer l'age de l'élève : ")
        classe = input("Entrer la classe de l'élève : ")
        ajout = cur.execute("INSERT INTO student VALUES (?,?,?)", (nom,age,classe))
        return ajout
    

print(ajoute("junior"))
