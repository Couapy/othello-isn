from random import *

tests = ((-1,  0), #on défini les coodonnées de vecteurs, lesquels permettront d'effectuer des tests dans le plateau de jeu
         ( 1,  0),
         ( 0, -1),
         ( 0,  1),
         (-1, -1),
         (-1, +1),
         ( 1, -1),
         ( 1,  1)
        )

def Jouer(grille, cases_possibles, joueur):
    #association de case(coordonées) à son nombre de pion qu'il retourne
    resultats = []
    for case in cases_possibles:
        x, y = case
        cases_retournees = 0
        for test in tests:
            e, f = test
            cases_retournees += Retourne(grille, joueur, x, y, e, f)
        resultats.append([case, cases_retournees])

    #sélection des cases qui retourne le plus de pion et donne une liste
    casemax = 0
    listemax = []
    for resultat in resultats:
        if casemax < resultat[1]:
            casemax = resultat[1]
            listemax = [resultat[0]]
        elif casemax == resultat[1]:
            listemax.append (resultat[0])

    #sélection de la case finalle
    if len (listemax) == 1:
        return listemax[0]
    else:
        case_ultime = [[0,0]]
        bord = 9
        for test in listemax:
            x, y = test
            bords = [x, y, 7-x, 7-y]
            bord_test = min(bords)
            if bord > bord_test:
                bord = bord_test
                case_ultime = [test]
            elif bord == bord_test:
                case_ultime.append(test)

        return choice(case_ultime)

def JoueurAdverse(joueur):
    if joueur == 1:
        return 2
    else:
        return 1

def Retourne(grille, joueur, x, y, e, f):
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
            elif grille[a][b] == JoueurAdverse(joueur): #si c'est un pion adverse, on continue
                temp = -2
            elif grille[a][b] == 0 or grille[a][b] == joueur: #si c'est du vide ou si c'est le pion du joueur, on arrête
                temp = -1
                stop = 1
    if temp > 0:
        return temp
    else:
        return 0
