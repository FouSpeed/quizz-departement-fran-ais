# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:29:47 2023

@author: felmy.thomas
"""

from variable import *
import time
import json
from fonction import *


#programme principale
mode_de_jeu = str(input("A quel mode voulez-vous jouer (n pour normale, m pour contre la montre, s pour sans erreur, r pour les records): "))

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

affichage_record(record['record_montre'], record['record_sans_fin'])
