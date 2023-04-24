import random


def choix_dept(dep:list, nbr_qst: int)->list:
    """
    Paramètres:
        dep: list - une liste de départements
        nbr_qst: int - un entier représentant le nombre de questions à poser

    Variables:
        dep_select: list - une liste vide qui sera remplie avec des dictionnaires contenant les informations des questions posées
        dep_deja_select: list - une liste vide qui stocke les départements déjà sélectionnés pour éviter de les poser plusieurs fois
        i: int - un entier qui itère sur la boucle "for" pour chaque question à poser
        deps_pour_dict: list - une liste vide qui sera remplie avec les trois départements choisis pour chaque question
        reponse_possible: list - une liste contenant les réponses possibles "a", "b" et "c"
        indice_dep_reponse: int - un entier qui stocke l'indice de la bonne réponse dans la liste "reponse_possible"
        dep_aleatoire: list - une liste contenant le nom et le numéro du département choisi au hasard
        dep_dict: dict - un dictionnaire contenant les informations de la question posée, avec les clés "dept", "a", "b", "c" et "bonne_reponse"
        j: int - un entier qui itère sur la boucle "for" pour chaque réponse possible dans le dictionnaire "dep_dict"

    Retour:
        dep_select: list - une liste de dictionnaires contenant les informations des questions posées, avec les clés
         "dept", "a", "b", "c" et "bonne_reponse"
    
    """
    dep_select = []
    dep_deja_select = []
    

    for i in range(nbr_qst):
        deps_pour_dict = []
        reponse_possible = ["a", "b", "c"]
        #mélanger reponse_possible
        reponse_possible = random_list(reponse_possible) #ou faire random.shuffle(reponse_possible)
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

        
        dep_dict = {
                "dept": deps_pour_dict[indice_dep_reponse][0],
                "a" : "",
                "b": "",
                "c": "", 
                "bonne_reponse" : reponse_possible[indice_dep_reponse]
                }
        
        #compléter les clés a,b,c de dep_dict
        for j in range (len(reponse_possible)):
            dep_dict[reponse_possible[j]] = deps_pour_dict[j][1]
        dep_select.append(dep_dict)

    return dep_select


        
def est_le_meilleur_chrono(nbr_dep: int, chrono: float, liste_chrono: list) -> bool:
    """
    Vérifie si le chrono donné est le meilleur pour le numéro de département donné, parmi une liste de chronos.

    Paramètres :
    ------------
    nbr_dep : int
        Le numéro de département à vérifier.
    chrono : float
        Le chrono à comparer avec les autres chronos pour ce numéro de département.
    liste_chrono : list
        La liste des chronos précédemment enregistrés, sous la forme d'une liste de tuples (chrono, numéro de département).

    Retour :
    --------
    bool
        True si le chrono donné est le meilleur pour ce numéro de département, False sinon.
    """
    for i in range(len(liste_chrono)):
        if liste_chrono[i][1] == nbr_dep and liste_chrono[i][0] < chrono:
            return False
    return True


def random_list(liste):
    """
    Paramètres :
        liste (list) : La liste d'éléments à mélanger.

    Variables :
        liste_random (list) : La liste aléatoire à remplir avec les éléments de la liste donnée.
        random_element (int) : L'élément aléatoire à ajouter à la liste aléatoire.

    Renvoie :
        list_random : list : La liste d'éléments mélangés aléatoirement.
    """
    liste_random = []
    while len(liste_random) != len(liste):
        random_element = liste[random.randint(0,len(liste))-1]
        if random_element not in liste_random:
            liste_random.append(random_element)
    return liste_random
