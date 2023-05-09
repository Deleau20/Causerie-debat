from tkinter import Entry
from string import ascii_letters, digits
from random import choice

def gen_mdp_into(widget: Entry):
    """Fonction qui génère un mot de passe"""
    default_length = 20

    mdp: str = ""
    while default_length > 0:
        mdp += choice(ascii_letters + digits)
        default_length -= 1
    
    if widget.get():
        
        widget.delete(0, widget.get().__len__())
    widget.insert(0, mdp)