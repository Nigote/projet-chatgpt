import os

for nom_fichier in os.listdir():
    if nom_fichier.endswith(".json"):
        os.remove(nom_fichier)
        print(f"Supprimé : {nom_fichier}")
