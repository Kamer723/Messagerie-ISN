from tkinter import *
from tkinter.messagebox import *
from pickle import*
fenetre = Tk()
scrollbar = Scrollbar(fenetre)
scrollbar.pack(side=RIGHT, fill=Y)
fenetre.geometry("400x200")
#liste des contact
liste = Listbox(fenetre,)
liste.insert(1, "Perso 1")
liste.insert(2, "Perso 2")
liste.insert(3, "Perso 3")
liste.insert(4, "Perso 4")
liste.insert(5, "Perso 5")
liste.pack(side=LEFT,padx=10, pady=10)
def alert():
    showinfo("alerte", "Bravo!")

def envoyer():
    labelmessages = Label(l, text=entree.get())
    labelmessages.pack()
    return

def envoi_text():
    labelmessages = Label(l, text=entree.get())
    labelmessages.pack()
    return
def callback(event):
    label["text"] = "You pressed Enter"
    

menubar = Menu(fenetre)
fenetre.bind('<Return>', callback)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.destroy)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)
#intergace avec les messages
l = LabelFrame(fenetre, text="Vos message", padx=20, pady=20, )
l.pack(fill="both", expand="yes",)
#for i in range(1,100):
#    labelframe.insert(END, "List " + str(i))
#scroll.config(command=LabelFrame)

# bouton pour envoyer un message
envoyer=Button(fenetre, text="Envoyer", command=envoyer)
envoyer.pack(side=RIGHT, padx=5, pady=5)
#Zones phrape de texte
value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=str, width=30)
entree.pack(side=BOTTOM , padx=10, pady=10)

fenetre.mainloop()
