import json


# retourne un tableau des possibles exos
def getData(part):
    with open('data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
    donnees[part]["exo"]
    return donnees[part]["exo"]


def addDataToFile():
    # TO DO
    return 0