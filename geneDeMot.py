from tkinter import Tk,Label, Entry, Button, Scale, HORIZONTAL, Frame, Widget
from tkinter.ttk import Combobox
from funcs import gen_mdp_into

def cmd():
    gen_mdp_into(entre)

def getPosition(maitre: Widget, enfant: Widget):
    m = maitre.winfo_width()
    e = enfant.winfo_width()
    milieu = (m//2) - (e//2)
    return milieu



root = Tk()
root.geometry("1000x600")
root.configure(bg="#0F3550")
root.title('Genérateur de mot de passe')
difficulty_box = Combobox(root, values=["Facile", "Difficile"])
frame = Frame(root, width=800, height=400, bg="#061745")
nom = Label(root, text="Bienvenue sur notre générateur", font=("Inter", 35), bg="#0F3550", foreground="white" )


label = Label(frame, text="Genérateur de mot de passe", bg="#061745", foreground="white", font=("Inter", 25))
entre = Entry(frame, width=50)
bouton = Button(frame, text="Génerer", command=cmd)
mdp_lenght = Scale(frame, from_=20, to=50, orient=HORIZONTAL)





# difficulty_box.pack()
# mdp_lenght.pack()
nom.pack()
frame.place(x=100, y=100)
label.place(x=0, y=0)
root.update()
label.place(x=getPosition(frame, label), y=0)
entre.place(x=getPosition(frame, entre), y=100)
root.mainloop()

