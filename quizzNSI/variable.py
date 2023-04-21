import json
DEPT_POUR_NORMALE = 10
DEPT_POUR_CONTRE_LA_MONTRE= 1
record_sans_erreur = 0
with open('record.json', 'r') as f:
    record = json.load(f)
record_temps_nbr_contre_la_montre = record["record_montre"] #liste de liste: (temps, nbr de département)
record_sans_erreur = record["record_sans_fin"]