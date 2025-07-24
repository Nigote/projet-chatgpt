from budget import ajouter_depense, ajouter_revenu, afficher_solde, initialiser_solde, afficher_historique



solde = initialiser_solde()
historique = {}
description = {}
while True :
    menu = input("""Que voulez vous faire ?:
                 1-Ajouter une dépense
                 2-Ajouter un revenu
                 3-Voir le solde
                 4-Afficher l'historique des transactions
                 0-Quitter
                 """)
    if menu == '1':
        montant = float(input("Entrez le montant de la dépense : "))
        description = input("A quoi correspond la dépense : ")
        solde, historique = ajouter_depense(solde, description, montant,historique)
    elif menu == '2':
        montant = float(input("Entrez le montant du revenu : "))
        description = input("A quoi correspond le revenu : ")
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
