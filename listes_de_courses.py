import json
import sys


def sauve(elem):
    with open('./courses.json', 'w+') as f:
        s = json.dumps(elem)
        f.write(s)
        


file = open("./courses.json", "r+")
r = file.read()
try:
    courses = json.loads(r)
except:
    courses = []

file.close()


# choisi une option
user_entrer = int(input("""
    Choisissez parmis les 5 options suivant:
    1 - Ajoutez un élément à la liste 
    2 - Retirer un élément de la liste
    3 - Afficher les éléments de la liste  
    ? Votre choix : >_ """
))


# si l'entrer est incorrect
if not 1 <= user_entrer <= 5:
    print("Veuillez choisir une option valide")

# execution en fonction de l'entrer
if user_entrer == 1:
    elem_ajouter = input("Entrer votre elelment : ")
    courses.append(elem_ajouter)
    print(f"L'élément {elem_ajouter} à bien été ajouté")
    sauve(courses)
    print(courses)
elif user_entrer == 2:
    print(courses)
    elem_sup = input("Entrer votre élément à retirer : ")
    if elem_sup in courses:
        courses.remove(elem_sup)
        print(f"L'élément {elem_sup} à bien été supprimer de la liste")
        sauve(courses)
        print(courses)
    else:
        print(f"L'élément {elem_sup} n'est pas dans la liste")
elif user_entrer == 3:
    if courses:
        for i,item in enumerate(courses):
            print(f"{i}.{item}")
    else:
        print("La liste est vide ")
else:
    print("Code")
