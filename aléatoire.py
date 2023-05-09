import random
import json

def randomword():
    tab = ["bonjour", "salut", "bonsoir"]
    return random.choice(tab)




if __name__ == '__main__':
    nombrechance = 3
    flag = False
    stargame = True
    mot = randomword()
    email = input("Entrez votre adresse email : ")
    motcache = ["*"]*len(mot)
    print("".join(motcache))


    

    while stargame:
        with open("./JeuEtoile.json", "r") as file:
            files = file.read()
            players = json.load(file)
            for player in players:            
                    if player["email"] == email:
                        print("vous avez déjà")



        car = input("\nEntrez un caractère : ")

        for i in range(len(mot)):
            if mot[i] == car:
              motcache[i] = car
              flag = True
                    

        if flag:
            flag = False
            print("Bingo !!!") 
        else:    
            nombrechance -= 1
            if nombrechance <= 0:
                print("Vous n'avez plus de chance")
                stargame = False
            else:
                print(f"Vous n'avez pas trouvé le caractère il vous reste {nombrechance}")

        output = "".join(motcache)
        print(output)
        if output == mot:
            stargame = False
        
