from time import sleep as wait
from tkinter import*
from tkinter.ttk import Progressbar
import csv
import os.path
import os

version="0.2 Français"

from tkinter.messagebox import *


def newgame():
    global nb_cookie
    global nb_craft
    global nbdefoisouilaaugmcraft
    global valeur_boulangerie
    global boulangerie
    global prix_boulanger
    if os.path.isfile("save.csv"):
        if askokcancel(title="Attention",message="Êtes-vous sur de vouloir créer un nouveau fichier ? L'ancien sera supprimé"):  
            os.remove('save.csv')
            nb_craft=1 #nb de craft de cookie par clic, valeur de base 1
            nb_cookie=0 #nb de cookie, valeur de base 0
            nbdefoisouilaaugmcraft=1 #nb de fois où on a amélioré le clic, valeur de base 1
            valeur_boulangerie=1 #nb cookie par seconde pour boulangerie, valeur de base 1
            boulangerie=0 # +1 cookie par seconde, valeur de base 0
            newpartie.pack_forget()
            continuepartie.pack_forget()
            lancement()
            prix_boulanger=10
    else:
        nb_craft=1 #nb de craft de cookie par clic, valeur de base 1
        nb_cookie=0 #nb de cookie, valeur de base 0
        nbdefoisouilaaugmcraft=1 #nb de fois où on a amélioré le clic, valeur de base 1
        valeur_boulangerie=1 #nb cookie par seconde pour boulangerie, valeur de base 1
        boulangerie=0 # +1 cookie par seconde, valeur de base 0
        prix_boulanger=10
        newpartie.pack_forget()
        continuepartie.pack_forget()
        lancement()

def continuer():
    global nb_cookie
    global nb_craft
    global nbdefoisouilaaugmcraft
    global valeur_boulangerie
    global boulangerie
    global prix_boulanger
    
    fichier = open("save.csv", "rt")
    lecteurCSV = csv.reader(fichier,delimiter=";")  # Ouverture du lecteur CSV en lui fournissant le caractère séparateur (ici ";")
    for ligne in lecteurCSV:
        if ligne!=[]:      
            if ligne[0]=="nb_cookie":
                nb_cookie=int(ligne[1])
            elif ligne[0]=="nb_craft":
                nb_craft=int(ligne[1])
            elif ligne[0]=="nbdefoisouilaaugmcraft":
                nbdefoisouilaaugmcraft=int(ligne[1])
            elif ligne[0]=="valeur_boulangerie":
                valeur_boulangerie=int(ligne[1])
            elif ligne[0]=="boulangerie":
                boulangerie=int(ligne[1])
            elif ligne[0]=="prix_boulanger":
                prix_boulanger=int(ligne[1])
    fichier.close()
    newpartie.pack_forget()
    continuepartie.pack_forget()
    lancement()
    
play=False
Avant_Jeu=Tk()
Labelle=Label(Avant_Jeu,text="Bienvenue dans Cookies Clicker Python !",font='Arial 25')
Labelle.pack()
sous_labelle=Label(Avant_Jeu,text="Version "+str(version),font='Arial 10')
sous_labelle.pack()
newpartie=Button(Avant_Jeu,text="Nouvelle partie",font="Arial 15",command=newgame)
newpartie.pack()
continuepartie=Button(Avant_Jeu,text="Continuer partie",font="Arial 15",command=continuer)
if not(os.path.isfile("save.csv")):
    continuepartie.config(state = DISABLED)
continuepartie.pack() 

def lancement():
    global play
    barre = Progressbar(Avant_Jeu,orient="horizontal", maximum=100, value=0)      
    barre.pack()
    def progress(currentValue):
        barre["value"]=currentValue
    currentValue=0
    maxValue=100
    barre["value"]=currentValue
    barre["maximum"]=maxValue
    divisions=10
    for i in range(divisions):
        currentValue=currentValue+10
        barre.after(100, progress(currentValue))
        barre.update() # Force an update of the GUI
        if barre["value"]==maxValue:
            Avant_Jeu.destroy()
            play=True
Avant_Jeu.mainloop()


def craft():
    global nb_cookie
    global nb_craft
    nb_cookie+=nb_craft
    cookie.config(text=nb_cookie)

def augm_clic():
    global nb_craft
    global nb_cookie
    global prix
    global prix_augm
    global nbdefoisouilaaugmcraft
    if nb_cookie>=prix:
        nbdefoisouilaaugmcraft+=1
        nb_craft=nb_craft*2
        nb_cookie-=prix
        cookie.config(text=nb_cookie)
        prix=5*(10**nbdefoisouilaaugmcraft)
        prix_augm="Coût: "+str(prix)
        text_craft="Fabriquer "+str(nb_craft)+" cookie"
        crafter.config(text=text_craft,command=craft,font="Arial 40")
        prix_augm_craft.config(text=prix_augm)
    else:
        a_afficher="Vous n'avez pas assez de cookies ! Il vous en manque "+str(prix-nb_cookie)
        add_console(a_afficher)

def boulanger():
    global nb_cookie
    global boulangerie
    global valeur_boulangerie
    global prix_boulanger
    global text_prix_boulanger
    nb_cookie+=boulangerie*valeur_boulangerie
    cookie.config(text=nb_cookie)
    Jeu.after(1000, boulanger)
    
def achat_boulangerie():
    global boulangerie
    global nb_cookie
    global prix_boulanger
    global text_nb_boulangerie
    if nb_cookie>=prix_boulanger:
        boulangerie+=1
        nb_cookie-=prix_boulanger
        cookie.config(text=nb_cookie)
        prix_boulanger=int(prix_boulanger*1.2)
        text_prix_boulanger="Coût :"+str(prix_boulanger)
        affiche_prix_boulanger.config(text=text_prix_boulanger)
        text_nb_boulangerie="Vous avez actuellement "+str(boulangerie)+" boulangeries"
        nb_boulangerie.config(text=text_nb_boulangerie)
    else:
        a_afficher="Vous n'avez pas assez de cookies ! Il vous en manque "+str(prix_boulanger-nb_cookie)
        add_console(a_afficher)

def achat_amelio_boulangerie():
    global valeur_boulangerie
    global nb_cookie
    global prix_amelio_boulanger
    global text_nb_amelio_boulangerie
    if nb_cookie>=prix_amelio_boulanger:
        valeur_boulangerie*=2
        nb_cookie-=prix_amelio_boulanger
        cookie.config(text=nb_cookie)
        prix_amelio_boulanger=int(prix_amelio_boulanger*10)
        text_prix_amelio_boulanger="Coût :"+str(prix_amelio_boulanger)
        affiche_prix_amelio_boulanger.config(text=text_prix_amelio_boulanger)
        text_nb_amelio_boulangerie="Vos boulangeries fabriquent "+str(valeur_boulangerie)+" cookies par secondes"
        nb_amelio_boulangerie.config(text=text_nb_amelio_boulangerie)
    else:
        a_afficher="Vous n'avez pas assez de cookies ! Il vous en manque "+str(prix_amelio_boulanger-nb_cookie)
        add_console(a_afficher)

def bots():
    boulanger()
    

Jeu =  Tk()
   
cookie=Label(Jeu, text=nb_cookie, background="cyan",font="Arial 70")
cookie.grid(column=0,row=0,rowspan=20,ipadx=250,ipady=200,sticky="EWNS")
text_craft="Fabriquer "+str(nb_craft)+" cookie"
crafter=Button(Jeu,text=text_craft,command=craft,font="Arial 40")
crafter.grid(column=0,row=21,ipady=50,sticky="EWNS")

info=Label(Jeu,text="Pour quitter, appuyez sur 'échap'",font='Arial 20')
info.grid(column=0,row=22,ipady=20,sticky="EWNS")
    

prix=5*(10**nbdefoisouilaaugmcraft)
prix_augm="Coût: "+str(prix)
prix_augm_craft=Label(Jeu,text=prix_augm,font="Arial 20")
augm_craft=Button(Jeu, text="Multiplier par 2 la puissance de vos clics !",command=augm_clic,font="Arial 20")
prix_augm_craft.grid(column=1,row=0,ipadx=20,ipady=20,sticky="EWNS")
augm_craft.grid(column=1,row=1,ipadx=30,ipady=20,sticky="EWNS")

Espace=Label(Jeu,text="     ",font="Arial 20")
Espace.grid(column=1,row=2,ipadx=30,ipady=20,sticky="EWNS")

text_prix_boulanger="Coût :"+str(prix_boulanger)
affiche_prix_boulanger=Label(Jeu,text=text_prix_boulanger,font='Arial 20')
acheter_boulangerie=Button(Jeu,text="Acheter 1 boulangerie",command=achat_boulangerie,font="Arial 20")
affiche_prix_boulanger.grid(column=1,row=3,ipadx=20,ipady=20,sticky="EWNS")
acheter_boulangerie.grid(column=1,row=4,ipadx=20,ipady=20,sticky="EWNS")
text_nb_boulangerie="Vous avez actuellement "+str(boulangerie)+" boulangeries"

nb_boulangerie=Label(Jeu,text=text_nb_boulangerie,font="Arial 20")
nb_boulangerie.grid(column=2,row=4,ipadx=20,ipady=20,sticky="EWNS")

nb_cookie+=boulangerie*1
cookie.config(text=nb_cookie)

Espace2=Label(Jeu,text="     ",font="Arial 20")
Espace2.grid(column=1,row=5,ipadx=30,ipady=20,sticky="EWNS")

prix_amelio_boulanger=100*(10**valeur_boulangerie)
text_prix_amelio_boulanger="Coût :"+str(prix_amelio_boulanger)
affiche_prix_amelio_boulanger=Label(Jeu,text=text_prix_amelio_boulanger,font='Arial 20')
acheter_amelio_boulangerie=Button(Jeu,text="Multiplier par 2 la cadence de vos boulangeries",command=achat_amelio_boulangerie,font="Arial 20")
affiche_prix_amelio_boulanger.grid(column=1,row=6,ipadx=20,ipady=20,sticky="EWNS")
acheter_amelio_boulangerie.grid(column=1,row=7,ipadx=20,ipady=20,sticky="EWNS")

text_nb_amelio_boulangerie="Vos boulangeries fabriquent "+str(valeur_boulangerie)+" cookies par secondes"
nb_amelio_boulangerie=Label(Jeu,text=text_nb_amelio_boulangerie,font="Arial 20")
nb_amelio_boulangerie.grid(column=2,row=7,ipadx=20,ipady=20,sticky="EWNS")

info=Label(Jeu,text="Derniers messages de la console:",font="Arial 20")
info.grid(column=2,row=0,ipadx=20,ipady=20,sticky="EWNS")
text_console="Il n'y a rien a dire"
message=Label(Jeu,text=text_console,font="Arial 15")
message.grid(column=2,row=1,ipadx=20,ipady=20,sticky="EWNS")

text1=""
text2=""
text3=""
text4=""
text5=""


def add_console(texte):
    global text_console
    global text1
    global text2
    global text3
    global text4
    global text5
    if text1=="":
        text1=texte
    elif text2=="":
        text2=text1
        text1=texte
    elif text3=="":
        text3=text2
        text2=text1
        text1=texte
    elif text4=="":        
        text4=text3
        text3=text2
        text2=text1
        text1=texte
    else:
        text5=text4
        text4=text3
        text3=text2
        text2=text1
        text1=texte
    text_console=text1+"\n"+text2+"\n"+text3+"\n"+text4+"\n"+text5
    message.config(text=text_console)
    

from tkinter.messagebox import *

def sauvegarder():
    fichier = open("save.csv", "wt")
    ecrivainCSV = csv.writer(fichier,delimiter=";")
    ecrivainCSV.writerow(["nb_cookie",nb_cookie])
    ecrivainCSV.writerow(["nb_craft",nb_craft])
    ecrivainCSV.writerow(["nbdefoisouilaaugmcraft",nbdefoisouilaaugmcraft])
    ecrivainCSV.writerow(["valeur_boulangerie",valeur_boulangerie])
    ecrivainCSV.writerow(["boulangerie",boulangerie])
    ecrivainCSV.writerow(["prix_boulanger",prix_boulanger])
    fichier.close()
    add_console("Sauvegarde effectué avec succès !")
def reinitialise():
    global nb_cookie
    global nb_craft
    global nbdefoisouilaaugmcraft
    global valeur_boulangerie
    global boulangerie
    global prix
    global prix_boulanger
    if askokcancel(title="Attention",message="Êtes-vous sur de vouloir réinitialiser votre partie ? Vous ne pourrez pas récupérer votre sauvegarde"):  
        nb_craft=1 #nb de craft de cookie par clic, valeur de base 1
        nb_cookie=0 #nb de cookie, valeur de base 0
        nbdefoisouilaaugmcraft=1 #nb de fois où on a amélioré le clic, valeur de base 1
        valeur_boulangerie=1 #nb cookie par seconde pour boulangerie, valeur de base 1
        boulangerie=0 # +1 cookie par seconde, valeur de base 0
        text_nb_boulangerie="Vous avez actuellement "+str(boulangerie)+" boulangeries"
        nb_boulangerie.config(text=text_nb_boulangerie)
        prix_boulanger=10
        prix_amelio_boulanger=1000
        text_prix_boulanger="Coût :"+str(prix_boulanger)
        affiche_prix_boulanger.config(text=text_prix_boulanger)
        text_prix_amelio_boulanger="Coût :"+str(prix_amelio_boulanger)
        affiche_prix_amelio_boulanger.config(text=text_prix_amelio_boulanger)
        text_nb_amelio_boulangerie="Vos boulangeries fabriquent "+str(valeur_boulangerie)+" cookies par secondes"
        nb_amelio_boulangerie.config(text=text_nb_amelio_boulangerie)
        prix=5*(10**nbdefoisouilaaugmcraft)
        sauvegarder()

autosave=False
tps_save=30000

def desact():
    global autosave
    autosave=False
    trente_s.config(state=DISABLED)
    une_min.config(state=DISABLED)
    deux_min.config(state=DISABLED)
    cinq_min.config(state=DISABLED)
    
def act():
    global autosave
    global trente_s, une_min, deux_min, cinq_min
    autosave=True
    trente_s.config(state=NORMAL)
    une_min.config(state=NORMAL)
    deux_min.config(state=NORMAL)
    cinq_min.config(state=NORMAL)

def trente():
    global tps_save
    tps_save=30000
def une():
    global tps_save
    tps_save=60000
def deux():
    global tps_save
    tps_save=120000
def cinq():
    global tps_save
    tps_save=300000
    
    
def auto_save():
    global autosave
    global tps_save
    if autosave:
        sauvegarder()
        
    Jeu.after(tps_save, auto_save)

def opt_save():
    global active
    global trente_s, une_min, deux_min, cinq_min
    active=BooleanVar()
    active.set(False)
    tps=IntVar()
    tps.set(30000)
    opt=Tk()
    Info=Label(opt,text="Option pour la sauvegarde automatique",font="Arial 22")
    yes=Radiobutton(opt, variable=active,text="Activer",value=True,command=act,font="Arial 30")
    no=Radiobutton(opt, variable=active,text="Désactiver",value=False,command=desact,font="Arial 30")
    Info2=Label(opt,text="Définissez le temps entre chaque sauvegarde automatique",font="Arial 20")
    Info3=Label(opt,text="Si vous voulez activez les options, vous devez bien cliquer dessus !",font="Arial 10")
    trente_s=Radiobutton(opt, variable=tps,text="30 s",value=30000,command=trente,font="Arial 15")
    une_min=Radiobutton(opt, variable=tps,text="1 min",value=60000,command=une,font="Arial 15")
    deux_min=Radiobutton(opt, variable=tps,text="2 min",value=120000,command=deux,font="Arial 15")
    cinq_min=Radiobutton(opt, variable=tps,text="5 min",value=300000,command=cinq,font="Arial 15")
    if active==False:
        trente_s.config(state=DISABLED)
        une_min.config(state=DISABLED)
        deux_min.config(state=DISABLED)
        cinq_min.config(state=DISABLED)
    Info2.grid(column=0,row=2,ipadx=20,ipady=20,columnspan=4,sticky="EWNS")
    Info3.grid(column=0,row=3,sticky="EWNS")
    trente_s.grid(column=0,row=6,ipadx=20,ipady=20)
    une_min.grid(column=1,row=6,ipadx=20,ipady=20)
    deux_min.grid(column=2,row=6,ipadx=20,ipady=20)
    cinq_min.grid(column=3,row=6,ipadx=20,ipady=20)
    yes.grid(column=0,row=5,ipadx=20,ipady=20,sticky="EWNS")
    no.grid(column=1,row=5,ipadx=20,ipady=20,sticky="EWNS")
    Info.grid(column=0,row=0,columnspan=4,ipady=20,sticky="EWNS")
    quitter=Button(opt,text="Quitter",command=opt.destroy)
    quitter.grid(column=0,row=7,ipadx=20,ipady=20,sticky="EWNS")

def quitter_par_echap():
    sauvegarder()
    quit()

def quitter_s_save():
    if askokcancel(title="Attention",message="Êtes-vous sur de vouloir quitter sans sauvegarder ? Votre progression sera perdu depuis votre dernière sauvegarde."):
        quit()


menubar = Menu(Jeu)
Jeu.config(menu=menubar)
menufichier = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Fichier", menu=menufichier)
menufichier.add_command(label="Enregistrer la partie",command=sauvegarder)
menufichier.add_command(label="Réinitialiser la partie",command=reinitialise)
menufichier.add_command(label="Option de sauvegarde automatique",command=opt_save)
menufichier.add_command(label="Quitter en sauvegardant",command=quitter_par_echap)
menufichier.add_command(label="Quitter sans sauvegarder",command=quitter_s_save)

"""C'est ici pour désactiver le plein écran"""

if play:
    
    Jeu.attributes('-fullscreen', True) #Remplassez 'True' par 'False' pour désactiver le plein écran
    
    
    Jeu.bind('<Escape>',lambda e: quit)
    Jeu.resizable(width=False, height=False)
    Jeu.after(1000, boulanger)
    Jeu.after(3000, auto_save)
    Jeu.mainloop()
else:
    quit()

