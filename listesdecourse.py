listes_de_courses = ["sac", "tomates", "viande"]

listes = int(input("Bienvenu, choisissez l'action à réaliser : \n1: Ajouter un élément dans la liste\n2: Rétirez un élément de la liste\n3: Voir la liste\n4: Videz la liste\n5: Supprimez la liste\n\n\nQuel est votre choix : >_"))
if not (1<= listes <=5) :
    
    print("Veuillez choisir une option valide : ")

if listes ==1:
    listes_de_courses.append(input("Donner le nom de l'élément à ajouter : "))

    print(listes_de_courses)

if listes ==2:
    item = input("Donner le nom de l'élément à rétirer : ")
    if item in listes_de_courses:
        listes_de_courses.remove(item)
        print(f"L'élément {item} à été rétiré ")
        nouv = " , ".join(listes_de_courses)
        print(f"voici la nouvelle liste de courses : {nouv} ")
    else:
        print(f"L'élément {item} n'est pas dans la liste ")


if listes ==3:
    print(listes_de_courses)




if listes ==4:
    listes_de_courses.remove()



if listes ==5:
     listes_de_courses.clear()
     print(listes_de_courses)