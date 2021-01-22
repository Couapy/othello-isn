from tkinter import *
from tkinter.messagebox import *

import IArandom
import IAfaible
import IAmoyen
import IAdifficile

fen = Tk()
fen.title("OTHELLO by l'a eu et Marchand")

joueur = j1 = j2 = scorej1 = scorej2 = grille = boutons = cases_possibles = aide = 0
partie_finie = True
joueur_en_cours = StringVar()
score1 = StringVar()
score2 = StringVar()

aidebouton = IntVar()

tests = ((-1,  0), #on défini les coodonnées de vecteurs, lesquels permettront d'effectuer des tests dans le plateau de jeu
         ( 1,  0),
         ( 0, -1),
         ( 0,  1),
         (-1, -1),
         (-1, +1),
         ( 1, -1),
         ( 1,  1)
        )

p1 = PhotoImage(file = "images/pions/1.png")
p2 = PhotoImage(file = "images/pions/2.png")
p3 = PhotoImage(file = "images/pions/3.png")
p4 = PhotoImage(file = "images/pions/4.png")
p5 = PhotoImage(file = "images/pions/5.png")
p6 = PhotoImage(file = "images/pions/6.png")
p7 = PhotoImage(file = "images/pions/7.png")
p8 = PhotoImage(file = "images/pions/8.png")

f1 = PhotoImage(file = "images/possible/1.png")
f2 = PhotoImage(file = "images/possible/2.png")
f3 = PhotoImage(file = "images/possible/3.png")
f4 = PhotoImage(file = "images/possible/4.png")

e1 = PhotoImage(file = "images/no/n1.png")
e2 = PhotoImage(file = "images/no/n2.png")
e3 = PhotoImage(file = "images/no/n3.png")
e4 = PhotoImage(file = "images/no/n4.png")

g1 = PhotoImage(file = "images/no/b1.png")
g2 = PhotoImage(file = "images/no/b2.png")
g3 = PhotoImage(file = "images/no/b3.png")
g4 = PhotoImage(file = "images/no/b4.png")

h1 = PhotoImage(file = "images/no/r1.png")
h2 = PhotoImage(file = "images/no/r2.png")
h3 = PhotoImage(file = "images/no/r3.png")
h4 = PhotoImage(file = "images/no/r4.png")

i1 = PhotoImage(file = "images/placer/b1.png")
i2 = PhotoImage(file = "images/placer/b2.png")
i3 = PhotoImage(file = "images/placer/b3.png")
i4 = PhotoImage(file = "images/placer/b4.png")
i5 = PhotoImage(file = "images/placer/n1.png")
i6 = PhotoImage(file = "images/placer/n2.png")
i7 = PhotoImage(file = "images/placer/n3.png")
i8 = PhotoImage(file = "images/placer/n4.png")

noir_blanc = [p1, p2, p3, p4, p6, p7, p8]
blanc_noir = [p8, p7, p6, p5, p3, p2, p1]
vide_pos = [f1, f2, f3, f4]
pos_vide = [f4, f3, f2, f1]
nope_noir = [e1, e2, e3, e4, e4, e3, e2, e1]
nope_blanc = [g1, g2, g3, g4, g4, g3, g2, g1]
nope_vide = [h1, h2, h3, h4, h4, h3, h2, h1]
placer_blanc = [i1, i2, i3, i4]
placer_noir = [i5, i6, i7, i8]

def Jouer(x, y, robot = False):
    global grille, partie_finie
    robots = ['ia0', 'ia1', 'ia2', 'ia3']
    if (joueur == 1 and j1 in robots and robot == True) or (joueur == 2 and j2 in robots and robot == True) or (((joueur == 1 and j1 == 'humain') or (joueur == 2 and j2 == 'humain')) and ([x,y] in cases_possibles and not partie_finie)):
        if aide and ((joueur == 1 and j1 == "humain") or (joueur == 2 and j2 == "humain")): #si le joueur précédent est un robot
            DesafficherCasesPossibles()
        RetournePions(x, y)
        JoueurSuivant()
        AfficherScore()
        CalculerCasesPossibles()

        if cases_possibles == []: #si le joueur ne peut pas Jouer
            JoueurSuivant() #on passe au joueur suivant
            CalculerCasesPossibles() #on recalcule les cases possibles pour l'autre joueur

            if cases_possibles == []: #si le second joueur ne peut pas Jouer, donc la partie est finie
                if not (j1 in robots) or not (j2 in robots):
                    if scorej1 > scorej2:
                        showinfo('Fin de partie !', 'Le joueur 1 a gagné la partie avec {} de points d\'avance'.format(scorej1 - scorej2))
                    elif scorej1<scorej2:
                        showinfo('Fin de partie !', 'Le joueur 2 a gagné la partie avec {} de points d\'avance'.format(scorej2 - scorej1))
                    else:
                        showinfo('Fin de partie !', 'Egalité parfaite !!')
                    Trier() #on affiche la proportion des pions
                partie_finie = True
            else:
                if aide and ((joueur == 1 and j1 == "humain") or (joueur == 2 and j2 == "humain")): #si le joueur n'est pas un robot
                    AfficherCasesPossibles() #tout s'est bien passé, on joue
                if not (j1 in robots) or not (j2 in robots):
                    showinfo('Information', 'Tu ne peux pas jouer ! Passes ton tour !')
                FaireJouerRobot() #on fait jouer les robots
        else:
            if aide and ((joueur == 1 and j1 == "humain") or (joueur == 2 and j2 == "humain")): #si le joueur n'est pas un robot
                AfficherCasesPossibles() #tout s'est bien passé, on joue
            FaireJouerRobot()  #on fait jouer les robots
    else:
        if partie_finie: #soit la partie est finie, soit elle n'a pas été lancée
            showinfo('Aucune partie en cours', 'Veuillez lancer une nouvelle partie...')
        elif grille[x][y] == 0:
            PlacerAnimation(x, y, 5) #on affiche l'animation vide impossible
        elif grille[x][y] == 1:
            PlacerAnimation(x, y, 6) #on affiche l'animation pion blanc impossible
        elif grille[x][y] == 2:
            PlacerAnimation(x, y, 7) #on affiche l'animation pion noir impossible

def FaireJouerRobot():
    robots = ['ia0', 'ia1', 'ia2', 'ia3']
    if (joueur == 1 and j1 in robots) or (joueur == 2 and j2 in robots): #c'est à un robot de jouer
        if joueur == 1:
            j = j1
        elif joueur == 2:
            j = j2

        if j == 'ia0':
            retour = IArandom.Jouer(cases_possibles) #on récupère la case que le robot veut jouer
        elif j == 'ia1':
            retour = IAfaible.Jouer(grille, cases_possibles, joueur) #on récupère la case que le robot veut jouer
        elif j == 'ia2':
            retour = IAmoyen.Jouer(grille, cases_possibles, joueur)
        elif j == 'ia3':
            retour = IAdifficile.Jouer(grille, cases_possibles, joueur)

        if j1 in robots and j2 in robots:
            delai = 150
        else:
            delai = 1500
        fen.after(delai, lambda: Jouer(retour[0], retour[1], True)) #après XXXms, le robot joue
    else:
        pass #c'est à l'humain de jouer, on ne fait rien

def JoueurSuivant():
    global joueur
    if joueur == 1:
        joueur = 2
        joueur_en_cours.set("Joueur 2 (pions noirs)")
    else:
        joueur = 1
        joueur_en_cours.set("Joueur 1 (pions blancs)")

def JoueurAdverse():
    global joueur
    if joueur == 1:
        return 2
    else:
        return 1

def CompterScore():
    global scorej1, scorej2
    a = 0
    b = 0
    for ligne in grille: #on parcours la grille
        for case in ligne:
            if case == 1: #et on compte le nombre de pions blancs
                a+= 1
            elif case == 2: #et de pions noirs
                b += 1
    scorej1 = a
    scorej2 = b

def AfficherScore():
    CompterScore()
    score1.set(scorej1)
    score2.set(scorej2)

def DesafficherCasesPossibles():
    for case in cases_possibles: #pour chacune des cases possibles
        PlacerAnimation(case[0], case[1], 4) #on fait jouer l'animation qui fait disparaitre la case possible

def AfficherCasesPossibles():
    for case in cases_possibles: #pour chacune des cases possibles
        PlacerAnimation(case[0], case[1], 3) #on fait jouer l'animation qui fait apparaitre la case possible

def CalculerCasesPossibles():
    global cases_possibles
    cases_possibles = []
    for x in range(0, 8): #on parcourir chaque case de la grille
        for y in range(0, 8):
            if grille[x][y] == 0: #si la case est vide
                temp = 0
                i = 0
                while temp == 0 and i != 8: #on va effectuer les tests jusqu'a que ce soit possible de joueur
                    test = tests[i]
                    i +=1
                    if casePossible(x, y, test[0], test[1]) == 1: #on teste si la case peut être jouée
                        case = [x,y]
                        cases_possibles.append(case) #on ajoute à notre liste de cases possibles
                        temp = 1 #on stope notre boucle, on passe à la case suivante

def casePossible(x, y, e, f):
    a = x
    b = y
    temp = False
    stop = 0
    while a+e <= 7 and a+e >= 0 and b+f <= 7 and b+f >= 0 and stop != 1: #si on est dans la grille, 0<x<7, 0<y<7
        a += e #on modifie les coordonées de la case qu'on va tester
        b += f
        #robots possibles de temp
        #-1 = pas bon : vide, ou on retourne pas de pions
        # 1 = bon, peut retourner

        if temp == False or temp == -2: #si c'est la première execution, et si on est sur une lignée de pions adverse
            if grille[a][b] == joueur and temp == -2: #si on peut encadrer les pions adverses
                temp = 1
                stop = 1
            elif grille[a][b] == JoueurAdverse(): #si c'est un pion adverse, on continue
                temp = -2
            elif grille[a][b] == 0 or grille[a][b] == joueur: #si c'est du vide ou si c'est le pion du joueur, on arrête
                temp = -1
                stop = 1

    return temp

def RetournePions(x,y):
    global grille
    if joueur == 1:
        anim = 8
    else:
        anim = 9
    grille[x][y] = joueur
    PlacerAnimation(x, y, anim)

    for test in tests: #on retourne les pions dans toutes les directions à partir de la case [x,y]
        e, f = test
        Retourne(x, y, e, f)

def Retourne(x, y, e, f):
    global grille
    a = x
    b = y
    c = 0
    temp = False
    stop = 0
    while a+e <= 7 and a+e >= 0 and b+f <= 7 and b+f >= 0 and stop != 1: #si on est dans la grille, 0<x<7, 0<y<7
        a += e
        b += f
        c += 1
        #-1 = vide
        #-2 = joueur adverse => attente
        #-1 = même joueur
        # 1 = bon, peut retourner

        if temp == False or temp == -2:
            if grille[a][b] == joueur and temp == -2:  #si on peut encadrer les pions adverses
                temp = c #on stocke la distance entre nos deux pions, entre les deux qui faut retourner
                stop = 1
            elif grille[a][b] == JoueurAdverse(): #si c'est un pion adverse, on continue
                temp = -2
            elif grille[a][b] == 0 or grille[a][b] == joueur: #si c'est du vide ou si c'est le pion du joueur, on arrête
                temp = -1
                stop = 1

    if temp > 0: #si on peut retourner
        a=x
        b=y
        if joueur == 1:
            anim = 2
        else:
            anim = 1
        for i in range(0, temp-1): #sur toute la distance où on retourne
            a += e
            b += f
            grille[a][b] = joueur
            PlacerAnimation(a, b, anim) #on execute l'aimation

def PlacerAnimation(x, y, a):
    if a == 1:
        i = 0
        for image in blanc_noir:
            i += 1
            delai = 50*i
            fen.after(delai, lambda image = image: afficher(x, y, image))
    elif a == 2:
        i = 0
        for image in noir_blanc:
            i += 1
            delai = 50*i
            fen.after(delai, lambda image = image: afficher(x, y, image))
    elif a == 3:
        i = 0
        for image in vide_pos:
            i += 1
            delai = 50*i
            fen.after(delai, lambda image = image: afficher(x, y, image))
    elif a == 4:
        i = 0
        for image in pos_vide:
            i += 1
            delai = 50*i
            fen.after(delai, lambda image = image: afficher(x, y, image))
    elif a == 5:
        i = 0
        for image in nope_vide:
            i += 1
            delai = 50*i
            fen.after(delai, lambda image = image: afficher(x, y, image))
    elif a == 6:
        i = 0
        for image in nope_blanc:
            i += 1
            delai = 50*i
            fen.after(delai, lambda image = image: afficher(x, y, image))
    elif a == 7:
        i = 0
        for image in nope_noir:
            i += 1
            delai = 50*i
            fen.after(delai, lambda image = image: afficher(x, y, image))
    elif a == 8:
        i = 0
        for image in placer_blanc:
            i += 1
            delai = 50*i
            fen.after(delai, lambda image = image: afficher(x, y, image))
    elif a == 9:
        i = 0
        for image in placer_noir:
            i += 1
            delai = 50*i
            fen.after(delai, lambda image = image: afficher(x, y, image))

def afficher(x, y, image):
    boutons[x][y].configure(image = image)

def Placer(j, x, y):
    if j == 0:
        boutons[x][y].configure(image = f1)
    elif j == 1:
        boutons[x][y].configure(image = p8)
    elif j == 2 :
        boutons[x][y].configure(image = p1)
    elif j == 3:
        boutons[x][y].configure(image = f4)

def Trier():
    i = 0
    for x in range(0,8):
        for y in range(0,8):
            i += 1
            if i <= scorej1:
                Placer(1, x, y)
            elif i <= scorej1 + scorej2:
                Placer(2, x, y)
            else:
                Placer(0, x, y)

def NouvellePartie():
    global j1, j2, partie_finie, aide
    robots = ['ia0', 'ia1', 'ia2', 'ia3']
    j1 = j1choix.get()
    j2 = j2choix.get()

    initialiser_variables()
    initialiser_grille()
    AfficherScore()

    aide = aidebouton.get()

    CalculerCasesPossibles()
    if j1 == "humain" and aide:
        AfficherCasesPossibles()
    else:
        FaireJouerRobot()

    partie_finie = False
    if not (j1 in robots) or not (j2 in robots):
        showinfo('Nouvelle partie !', 'C\'est parti moussaillon ! En avant pour la bataille !!')

def initialiser_variables():
    global grille, joueur, boutons, scorej1, aide
    grille = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,1,2,0,0,0],
        [0,0,0,2,1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
        ]
    boutons = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,1,2,0,0,0],
        [0,0,0,2,1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
        ]
    joueur = 1
    aide = 1

def initialiser_grille():
    global grille, boutons
    for x in range(0,8):
        for y in range(0,8):
            boutons[x][y] = Button(fen, image = f1, command = lambda x = x, y = y : Jouer(x,y))
            boutons[x][y].grid(row = x, column = y)
            Placer(grille[x][y], x, y)
    CalculerCasesPossibles()

def initialiser_graphique():
    global j1choix, j2choix
    initialiser_grille()

    Label(fen, text="OTHELLO", font=(32)).grid(row=0, column=8)
    cadre = Frame(fen, borderwidth=2, relief=GROOVE)
    cadre.grid(row=1, column=8, rowspan=3)
    Label(cadre, text="Joueur 1", font=(16)).grid(row=0, column=0)
    Label(cadre, text="Joueur 2", font=(16)).grid(row=0, column=1)

    robots = ['humain', 'ia0', 'ia1', 'ia2', 'ia3']
    texte = ['Humain', 'Ordinateur rigolo','Ordinateur facile', 'Ordinateur moyen', 'Ordinateur difficile']
    j1choix = StringVar()
    j1choix.set(robots[0])
    for i in range(len(texte)):
        Radiobutton(cadre, variable=j1choix, text=texte[i], value=robots[i]).grid(row=i+1, column=0)
    j2choix = StringVar()
    j2choix.set(robots[0])
    for i in range(len(texte)):
        Radiobutton(cadre, variable=j2choix, text=texte[i], value=robots[i]).grid(row=i+1, column=1)

    Button(cadre, text="Lancer une nouvelle partie", command=NouvellePartie).grid(row=6, column=0, columnspan=2)
    test = Checkbutton (cadre, variable = aidebouton, text="Afficher les aides", onvalue = 1, offvalue = 0)
    test.grid(row=7, column=0, columnspan=2)
    test.select()    
    
    Label(fen, textvariable = joueur_en_cours, font=(20)).grid(row=4, column=8)
    joueur_en_cours.set("Joueur 1 (pions blancs)")

    scores = Frame(fen, borderwidth=2, relief=GROOVE)
    scores.grid(row=5, column=8, rowspan=3)
    Label(scores, text = "Scores", font = ("Helvetica", 20)).grid(row=0, column=0, columnspan=2)
    Label(scores, text = "Joueur 1", font = (24)).grid(row=1, column=0)
    Label(scores, text = "Joueur 2", font = (24)).grid(row=1, column=1)
    Label(scores, textvariable = score1, font = (24)).grid(row=2, column=0)
    Label(scores, textvariable = score2, font = (24)).grid(row=2, column=1)

    AfficherScore()

initialiser_variables()
initialiser_graphique()

fen.mainloop()
