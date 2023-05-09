from tkinter import Entry
from string import ascii_letters, digits
from random import choice

def niveau(widget: Entry):
    """Fonction qui génère un niveau en fonction de la difficulté choisi"""
    END = ""
    if widget.get() == "1":
        widget.delete(0, END)
        widget.insert(0, "1")
    elif widget.get() == "2":
        widget.delete(0, END)
        widget.insert(0, "2")
    elif widget.get() == "3":
        widget.delete(0, END)
        widget.insert(0, "3")
    elif widget.get() == "4":
        widget.delete(0, END)
        widget.insert(0, "4")
    elif widget.get() == "5":
        widget.delete(0, END)
        widget.insert(0, "5")
    elif widget.get() == "6":
        widget.delete(0, END)
        widget.insert(0, "6")
    elif widget.get() == "7":
        widget.delete(0, END)
        widget.insert(0, "7")
    elif widget.get() == "8":
        widget.delete(0, END)
        widget.insert(0, "8")
    elif widget.get() == "9":
        widget.delete(0, END)
        widget.insert(0, "9")
    elif widget.get() == "10":
        widget.delete(0, END)
        widget.insert(0, "10")