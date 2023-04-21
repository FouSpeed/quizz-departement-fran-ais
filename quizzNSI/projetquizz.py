# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:29:47 2023

@author: felmy.thomas
"""

import random
from variable import *
import time
import json




def choix_dept(dep:list, nbr_qst: int):
    dep_select = []
    dep_deja_select = []
    

    for i in range(nbr_qst):
        deps_pour_dict = []
        reponse_possible = ["a", "b", "c"]
        #mélanger reponse_possible
        random.shuffle(reponse_possible)
        #la bonne réponse sera le premier élément de reponse_possible
        indice_dep_reponse = 0 
        #choix des 3 département à mettre dans le dictionnaire
        while len(deps_pour_dict) != 3:
            dep_aleatoire = dep[random.randint(0,len(dep)-1)]
            if dep_aleatoire not in dep_deja_select:
                deps_pour_dict.append(dep_aleatoire)
                #permettre à ce que le département soit posé en question qu'une seule fois
                if len(deps_pour_dict) == indice_dep_reponse:
                    dep_deja_select.append(dep_aleatoire)

        
        dep_dict = {"dept": deps_pour_dict[indice_dep_reponse][0], "a" : "", "b": "" , "c": "", 
                    "bonne_reponse" : reponse_possible[indice_dep_reponse]}
        #compléter les clés a,b,c de dep_dict
        for j in range (len(reponse_possible)):
            dep_dict[reponse_possible[j]] = deps_pour_dict[j][1]

        dep_select.append(dep_dict)
    return dep_select

        
def est_le_meilleur_chrono(nbr_dep:int, chrono:float, liste_chrono:list)->bool:
    for i in range(len(liste_chrono)):
        if liste_chrono[i][1] == nbr_dep and liste_chrono[i][0] < chrono:
            return False
    return True






departement=[['Ain', 1], ['Aisne', 2], ['Allier', 3], ['Alpes-de-Haute-Provence', 4], ['Hautes-Alpes', 5], 
             ['Alpes-Maritimes', 6], ['Ardèche', 7], ['Ardennes', 8], ['Ariège', 9], ['Aube', 10],
             ['Aude', 11], ['Aveyron', 12], ['Bouches-du-Rhône', 13], ['Calvados', 14], ['Cantal', 15],
             ['Charente', 16], ['Charente-Maritime', 17], ['Cher', 18], ['Corrèze', 19], ['Corse', 20],
             ["Côte-d'Or", 21], ["Côtes-d'Armor", 22], ['Creuse', 23], ['Dordogne', 24], ['Doubs', 25],
             ['Drôme', 26], ['Eure', 27], ['Eure-et-Loir', 28], ['Finistère', 29], ['Gard', 30],
             ['Haute-Garonne', 31], ['Gers', 32], ['Gironde', 33], ['Hérault', 34], ['Ille-et-Vilaine', 35], ['Indre', 36],
             ['Indre-et-Loire', 37], ['Isère', 38], ['Jura', 39], ['Landes', 40], ['Loir-et-Cher', 41], ['Loire', 42],
             ['Haute-Loire', 43], ['Loire-Atlantique', 44], ['Loiret', 45], ['Lot', 46], ['Lot-et-Garonne', 47], ['Lozère', 48],
             ['Maine-et-Loire', 49], ['Manche', 50], ['Marne', 51], ['Haute-Marne', 52], ['Mayenne', 53],
             ['Meurthe-et-Moselle', 54], ['Meuse', 55], ['Morbihan', 56], ['Moselle', 57], ['Nièvre', 58],
             ['Nord', 59], ['Oise', 60], ['Orne', 61], ['Pas-de-Calais', 62], ['Puy-de-Dôme', 63], ['Pyrénées-Atlantiques', 64],
             ['Hautes-Pyrénées', 65], ['Pyrénées-Orientales', 66], ['Bas-Rhin', 67], ['Haut-Rhin', 68],
             ['Rhône', 69], ['Haute-Saône', 70], ['Saône-et-Loire', 71], ['Sarthe', 72], ['Savoie', 73],
             ['Haute-Savoie', 74], ['Paris', 75], ['Seine-Maritime', 76], ['Seine-et-Marne', 77], ['Yvelines', 78],
             ['Deux-Sèvres', 79], ['Somme', 80], ['Tarn', 81], ['Tarn-et-Garonne', 82], ['Var', 83], ['Vaucluse', 84],
             ['Vendée', 85], ['Vienne', 86], ['Haute-Vienne', 87], ['Vosges', 88], ['Yonne', 89], ['Territoire de Belfort', 90],
             ['Essonne', 91], ['Hauts-de-Seine', 92], ['Seine-Saint-Denis', 93], ['Val-de-Marne', 94], ["Val-d'Oise", 95]] 


#programme principale
mode_de_jeu = str(input("A quel mode voulez-vous jouer (n pour normale, m pour contre la montre, s pour sans erreur): "))

point = 0
if mode_de_jeu == "n":
    dept_selec = choix_dept(departement, DEPT_POUR_NORMALE)
    for i in range(len(dept_selec)):
        print(f"quel est le numéro de département de {dept_selec[i]['dept']}:\na: {dept_selec[i]['a']}\nb: {dept_selec[i]['b']}\nc: {dept_selec[i]['c']}")
        reponse_joueur = str(input("votre réponse : "))
        if reponse_joueur == dept_selec[i]["bonne_reponse"]:
            point += 1
            print('\nBonne réponse !\n')
        else:
            print(f"\nMauvaise réponse, la réponse était {dept_selec[i]['bonne_reponse']}\n")
    print(f'votre score est de {point}/{len(dept_selec)}')

elif mode_de_jeu == "m":
    dept_selec = choix_dept(departement, DEPT_POUR_CONTRE_LA_MONTRE)
    print(f"Vous devez répondre le plus rapidement aux {DEPT_POUR_CONTRE_LA_MONTRE} questions suivantes")
    #compte à rebourd
    for j in range(3, -1, -1):
        time.sleep(1)
        print(f"début dans {j} secondes\n")

    continuer = True
    start_time = time.time()
    for i2 in range(len(dept_selec)):
        if continuer:
            print(f"quel est le numéro de département de {dept_selec[i2]['dept']}:\na: {dept_selec[i2]['a']}\nb: {dept_selec[i2]['b']}\nc: {dept_selec[i2]['c']}")
            reponse_joueur = str(input("votre réponse : "))
            if reponse_joueur == dept_selec[i2]["bonne_reponse"]:
                print('\nBonne réponse !\n')
            else:
                print(f"\nMauvaise réponse, la réponse était {dept_selec[i2]['bonne_reponse']}\n Vous avez perdu")
                continuer = False
    end_time = time.time()
    chrono = round(end_time - start_time, 2)
    if continuer:
        print(f'vous avez répondu à {DEPT_POUR_CONTRE_LA_MONTRE} questions en {chrono}')
        if est_le_meilleur_chrono(DEPT_POUR_CONTRE_LA_MONTRE, chrono, record_temps_nbr_contre_la_montre):
            record["record_montre"].insert(0, [chrono, DEPT_POUR_CONTRE_LA_MONTRE])
            print("votre chrono est un record")
            with open('record.json', 'w') as f:
                json.dump(record, f)
            print(record_temps_nbr_contre_la_montre)
elif mode_de_jeu == "s":
    dept_selec = choix_dept(departement, 95)
    print(f"Votre but est de répondre au plus grand nombre de questions possible\n record: {record_sans_erreur}")
    continuer = True
    bonne_reponse = 0
    for i3 in range(len(dept_selec)):
        if continuer:
            print(f"quel est le numéro de département de {dept_selec[i3]['dept']}:\na: {dept_selec[i3]['a']}\nb: {dept_selec[i3]['b']}\nc: {dept_selec[i3]['c']}")
            reponse_joueur = str(input("votre réponse : "))
            if reponse_joueur == dept_selec[i3]["bonne_reponse"]:
                bonne_reponse += 1
                print('\nBonne réponse !\n')
            else:
                print(f"\nMauvaise réponse, la réponse était {dept_selec[i3]['bonne_reponse']}\n")
                continuer = False
            print(f'votre score est de {bonne_reponse}/95')
    if bonne_reponse > record_sans_erreur:
        print(f"Vous avez battu l'ancien record de {record_sans_erreur}")
        record["record_sans_fin"] = bonne_reponse
        with open('record.json', 'w') as f:
            json.dump(record, f)

print(f"Voici les record:\npour contre la montre: {record['record_montre']}\npour le questionnaire sans fin: {record['record_sans_fin']}")

