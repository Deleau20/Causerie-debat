import random
import json

def randomword():
    tab = ["bonjour", "salut", "bonsoir"]
    return random.choice(tab)

if __name__ == '__main__':
    nombrechance = 3
    flag = False
    stargame = True
    email = input("Entrez votre adresse email : ")
    mot = randomword()
    motcache = ["*"] * len(mot)
    print("".join(motcache))


    # Vérifier si l'email existe déjà dans le fichier json
    with open("./JeuEtoile.json", "r") as file:
        files = file.read()
        players = json.loads(files)
        for player in players:
            if player["email"] == email:

                # Charger le jeu sauvegardé
                mot = player["mot"]
                motcache = player["motcache"]
                nombrechance = player["nombrechance"]
                print("Jeu chargé avec succès.")
                print("".join(motcache))
                break

        

    while stargame:
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
            print("Félicitations, vous avez gagné !")
            stargame = False

    # Sauvegarder le jeu pour le joueur actuel
    new_player = {
        "email": email,
        "mot": mot,
        "motcache": motcache,
        "nombrechance": nombrechance,
    }
    with open("./JeuEtoile.json", "w") as file:
        players.append(new_player)
        json.dump(players, file)