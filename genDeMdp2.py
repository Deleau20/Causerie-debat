import tkinter as tk
from tkinter import ttk
from tkinter import Entry
from string import ascii_letters, digits
from random import choice

class PasswordGeneratorApp:

    def _init_(self, master):
        self.master = master
        master.title("Générateur de mot de passe")

        # Ajouter une boîte de sélection pour choisir la difficulté
        self.difficulty_label = ttk.Label(master, text="Difficulté:")
        self.difficulty_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.difficulty_box = ttk.Combobox(master, values=["facile", "difficile"])
        self.difficulty_box.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.difficulty_box.current(0) # Sélectionner "facile" par défaut

        # Ajouter une barre de défilement pour choisir la longueur du mot de passe (pour la difficulté difficile)
        self.length_label = ttk.Label(master, text="Longueur:")
        self.length_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.length_scale = tk.Scale(master, from_=10, to=50, orient=tk.HORIZONTAL)
        self.length_scale.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.length_scale.set(20) # Définir la longueur par défaut à 20

        # Ajouter un champ d'entrée pour afficher le mot de passe généré
        self.password_label = ttk.Label(master, text="Mot de passe:")
        self.password_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.password_entry = Entry(master, show="*")
        self.password_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Ajouter un bouton pour générer le mot de passe
        self.generate_button = ttk.Button(master, text="Générer", command=self.on_generate_clicked)
        self.generate_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")

    def on_generate_clicked(self):
        difficulty = self.difficulty_box.get()

        if difficulty == "difficile":
            length = self.length_scale.get()
        else:
            length = 20

        self.gen_mdp_into(self.password_entry, length=length) # type: ignore

    def gen_mdp_into(self, widget: Entry, length: int = 20):
        """Fonction qui génère un mot de passe"""
        mdp: str = ""
        while length > 0:
            mdp += choice(ascii_letters + digits)
            length -= 1
    
        if widget.get():
            widget.delete(0, widget.get()._len_()) # type: ignore
        widget.insert(0, mdp)

root = tk.Tk()
app = PasswordGeneratorApp(root) # type: ignore
root.mainloop()