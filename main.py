import json
import os
import re

from budget import ajouter_depense, ajouter_revenu, afficher_solde, initialiser_solde, afficher_historique

# Initialisation du solde et de l'historique

user_name = input("Quelle est votre nom ? ").strip()
user_name = re.sub(r"[^\w\-]", "_", user_name)  # Nettoyage du nom d'utilisateur
user_file = f"{user_name}_solde.json"

if os.path.exists(user_file):
    
    with open(user_file, 'r') as file:
        data = json.load(file)
        solde = data.get('solde', 0)
        historique = data.get('historique', [])
        print(f"Bonjour, {user_name}, bienvenue! Vos données ont été chargées.")

else:
    solde = initialiser_solde()
    historique = []
    print(f'Bonjour, {user_name}, bienvenue! Vos données ont été initialisées.')




description = {}
while True :
    menu = input("""
    Que voulez vous faire ?:
        1-Ajouter une dépense
        2-Ajouter un revenu
        3-Voir le solde
        4-Afficher l'historique des transactions
        0-Quitter
        Votre choix : """)
    if menu == '1':
        date = input("Entrez la date de la dépense (A/M/J) : ")
        desc = input("Entrez la description de la dépense : ")     
        montant = input("Entrez le montant de la dépense : ")
        while not montant.isdigit():  
            print("Veuillez entrer un montant valide.")
            montant = input("Entrez le montant de la dépense : ")
        montant = float(montant)
        montant = -1*montant
        description = {'date': date, 'description': desc, 'montant': montant}
        solde, historique = ajouter_depense(solde, description, montant,historique)
    elif menu == '2':
        date = input("Entrez la date du revenu (A/M/J) : ")
        desc = input("Entrez la description du revenu : ")
        montant = input("Entrez le montant du revenu : ")
        while not montant.isdigit():
            print("Veuillez entrer un montant valide.")
            montant = input("Entrez le montant du revenu : ")
        montant = float(montant)
        description = {'date': date, 'description': desc, 'montant': montant}
        solde, historique = ajouter_revenu(solde, description, montant, historique)
    elif menu == '3':
        solde = afficher_solde(solde)
    elif menu == '4':
        afficher_historique(historique, solde)
    
    elif menu == '0':
        print("Merci d'avoir utilisé notre service. Au revoir!")
        break
    else :
        print("Option invalide, veuillez réessayer.")

    

# Sauvegarde des données

data = {
    'solde': solde,
    'historique': historique
}


with open(user_file, "w") as fichier:
    json.dump(data, fichier, indent=4)
    

