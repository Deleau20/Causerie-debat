duree = input("Entrez la duree en nombre de jour : ")
kilomètre = input("Entrez une distance en kilomètre : ")
deasel =0
essence =0



try :
    if type(duree) is not float and type(kilomètre) is not int:
        essence = (15*duree)+(0.85*kilomètre)
        deasel = (16*duree)+(0.66*kilomètre)
    print(essence,deasel)

except :
    print("Veuillez entrez des valeurs corrects")

else:
    
    if deasel > essence:
        print("Je vous conseil de choisir l'essence.")
    else:
        print("Je vous conseil de choisir le deasel")