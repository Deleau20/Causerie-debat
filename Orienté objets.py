import random

# class Homme:

#     def __init__(self, nom: str, nourriture: str, nbPas: int=1):
#         self.nourriture = nourriture
#         self.nom = nom
#         self.nbPas = nbPas

#     def sePresenter(self):
#         return f"je m'appelle {self.nom} "


#     def marcher(self):
#         return f"j'avance de {self.nbPas} pas  "



#     def manger(self):
#         return f"je mange : {self.nourriture} "


# frejus = Homme("junior","garba",3)
# print(frejus.manger())
# print(frejus.sePresenter())
# print(frejus.marcher())


# class Animal:

#     def __init__(self, breed, types, leg: int, form, color, shout, force: int=10):
#         self.breed = breed
#         self.types = types
#         self.leg = leg
#         self.form = form
#         self.color = color
#         self.shout = shout
#         self.force = force
    
#     def make_shout(self):
#         return self.shout

#     def attack(self, nb):
#         self.force = nb
#         if nb < self.force:
#             return "Vous avez perdu"
#         return "vous avez gagnez"

#     def move(self):
#         print("j'avance d'un pas")

# lion = Animal("felin","predator",4,"grand","gris","rugis",10)
# chat = Animal("felin","predator",4,"petit","gris","miole",8)
# print(lion.attack(chat)) 

class Personnages:

    def __init__(self):
        self.point=0

    def rollDice(self):
        self.point+=random.randint(1,6)

    def getResult(self):
        return self.point
        

p1=Personnages()
p2=Personnages()

for i in range(3):
    p1.rollDice()
    p2.rollDice()

if p1.getResult() > p2.getResult():
    print(f"p1 gagne avec {p1.getResult()} points et p2 à : {p2.getResult()} points")
elif p1.getResult() < p2.getResult():
    print(f"p2 gagne avec {p2.getResult()} points et p1 à : {p1.getResult()} points ")

else:
    print(f"Egalité p1= {p1.getResult()} points et p2= {p2.getResult()} points ")
