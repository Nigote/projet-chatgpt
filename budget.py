

def initialiser_solde():
    user_name = input("Quelle est votre nom ? ")
    print(f"Bonjour, {user_name}, bienvenue!")
    solde = int(input("Quel est votre solde actuel ? "))
    return solde

def ajouter_depense(solde, description, montant, historique):
    """Ajoute une dépense au solde."""
    solde -= montant
    print(f"Votre nouvelle dépense de {montant} a été enregistrée. Nouveau solde : {solde}")
    historique[description] = -montant
    return solde, historique

def ajouter_revenu(solde, description, montant, historique):
    """Ajoute un revenu au solde."""
    solde += montant
    print(f"Votre nouveau revenu de {montant} a été enregistré. Nouveau solde : {solde}")
    historique[description] = montant
    return solde, historique

def afficher_solde(solde):  
    """Affiche le solde actuel."""
    print(f"Votre solde actuel est : {solde}")
    return solde

def afficher_historique(historique, solde):
    """Affiche l'historique des transactions."""
    if not historique:
        print("Aucune transaction enregistrée.")
        print(f'Votre solde actuel est : {solde}')
    else:
        print("Historique des transactions :")
        for transaction in historique:
            print(transaction, ":", historique[transaction])
    print(f'Votre solde actuel est : {solde}')