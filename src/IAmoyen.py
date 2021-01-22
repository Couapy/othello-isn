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
	#association de case(coordonées) à son coefficient
	resultats = []
	j2 = JoueurAdverse(joueur)
	for case in cases_possibles:
		#notre robot
		x, y = case
		cases_retournees = 0
		grille_temp = list(map(list, grille))
		for test in tests:
			e, f = test
			resultat = Retourne(grille_temp, joueur, x, y, e, f)
			cases_retournees += resultat[1]
			grille_temp = resultat[0]
			grille_temp[x][y] = joueur

		#joueur adverse
		cases_pos_ad = CalculerCasesPossibles(j2, grille_temp)
		resultat_ad = []
		if len(cases_pos_ad) != 0:
			for case_ad in cases_pos_ad:
				grille_temp_ad = list(map(list, grille_temp))
				x, y = case_ad
				cases_retournees_ad = 0

				for test in tests:
					e, f = test
					resultat = Retourne(grille_temp_ad, j2, x, y, e, f)
					cases_retournees_ad += resultat[1]
					grille_temp_ad = resultat[0]
					grille_temp_ad[x][y] = j2
				resultat_ad.append([case_ad, cases_retournees_ad])
			max_ad = 0
			for case_max in resultat_ad:
				if case_max[1] > max_ad:
					max_ad = case_max[1]
		else:
			max_ad = 1

		#calcul de coef
		coef = cases_retournees / max_ad
		resultats.append([case, coef])

	#sélection des cases qui ont le meilleur coefficient et donne une liste
	casemax = 0
	listemax = []
	for resultat in resultats:
		if casemax < resultat[1]:
			casemax = resultat[1]
			listemax = [resultat[0]]
		elif casemax == resultat[1]:
			listemax.append (resultat[0])

	#sélection de la case finalle
	return choice(listemax)

def CalculerCasesPossibles(joueur, grille):
	cases_possibles = []
	for x in range(0, 8): #on parcourir chaque case de la grille
		for y in range(0, 8):
			if grille[x][y] == 0: #si la case est vide
				temp = 0
				i = 0
				while temp == 0 and i != 8: #on va effectuer les tests jusqu'a que ce soit possible de joueur
					test = tests[i]
					i +=1
					if casePossible(x, y, test[0], test[1], grille, joueur) == 1: #on teste si la case peut être jouée
						case = [x,y]
						cases_possibles.append(case) #on ajoute à notre liste de cases possibles
						temp = 1 #on stope notre boucle, on passe à la case suivante
	return cases_possibles

def casePossible(x, y, e, f, grille, joueur):
	a = x
	b = y
	temp = False
	stop = 0
	while a+e <= 7 and a+e >= 0 and b+f <= 7 and b+f >= 0 and stop != 1: #si on est dans la grille, 0<x<7, 0<y<7
		a += e #on modifie les coordonées de la case qu'on va tester
		b += f
		#valeurs possibles de temp
		#-1 = pas bon : vide, ou on retourne pas de pions
		# 1 = bon, peut retourner

		if temp == False or temp == -2: #si c'est la première execution, et si on est sur une lignée de pions adverse
			if grille[a][b] == joueur and temp == -2: #si on peut encadrer les pions adverses
				temp = 1
				stop = 1
			elif grille[a][b] == JoueurAdverse(joueur): #si c'est un pion adverse, on continue
				temp = -2
			elif grille[a][b] == 0 or grille[a][b] == joueur: #si c'est du vide ou si c'est le pion du joueur, on arrête
				temp = -1
				stop = 1

	return temp

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
		if temp == False:
			if grille[a][b] == joueur and temp == -2:  #si on peut encadrer les pions adverses
				temp = c #on stocke la distance entre nos deux pions, entre les deux qui faut retourner
				stop = 1
			elif grille[a][b] == JoueurAdverse(joueur): #si c'est un pion adverse, on continue
				temp = False
			elif grille[a][b] == 0 or grille[a][b] == joueur: #si c'est du vide ou si c'est le pion du joueur, on arrête
				temp = 0
				stop = 1

	a=x
	b=y
	for i in range(0, temp-1): #sur toute la distance où on retourne
		a += e
		b += f
		grille[a][b] = joueur
	return [grille, c]
