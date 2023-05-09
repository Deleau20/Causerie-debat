import sqlite3

conn = sqlite3.connect("./moko.db")

cur = conn.cursor()

class Student:

    def __init__(self):
        self.conn = sqlite3.connect("./moko.db")
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS student(
        id INTEGER  PRIMARY KEY,
        nom TEXT,
        age INTEGER,
        classe TEXT
        )''')

    def add_student(self, nom, age,classe):
        self.cur.execute("""INSERT INTO student(nom, age, classe) VALUES(?, ?, ?)""", ("fred", 15, "NaN"))
        self.conn.commit()

    def get_all_student(self):
        pass

    def get_student(self):
        pass

    def update(self):
        pass

    def delate(self):
        pass







eleve1 = Student()

def ajoute():
    nom=input("Entrer un nom")
    if type(nom) !=str or nom == '':
        nom = nom=input("Veuillez remplir le champ du nom")
    age=input("Entrer un age")
    if not isinstance(age, int) or age == 0:
        age=input("Veuillez remplir le champ du age")
    classe=input("Entrer un classe")
    if classe == '':
        classe = classe=input("Veuillez remplir le champ de la classe")

    eleve1.add_student(nom,age,classe)

def affiche():
    return eleve1.get_all_student()

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
    affiche()

elif user_entrer == 2:
    ajoute()