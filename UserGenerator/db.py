import sqlite3
from dataclasses import dataclass

try:
        conn = sqlite3.connect('my.db')
        sql = '''CREATE TABLE person (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        address TEXT NOT NULL
                );'''
        cur = conn.cursor()
        print("Connexion réussie à SQLite")
        cur.execute(sql)
        conn.commit()
        print("Table SQLite est créée")
        cur.close()
        conn.close()
        print("Connexion SQLite est fermée")
except sqlite3.Error as error:
     print("Erreur lors de la création du table SQLite", error)

@dataclass
class User:
    nom: str
    prenom: str
    email: str
    mdp: str
    birthday: str