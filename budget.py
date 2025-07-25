

def initialiser_solde():
    while type(solde := input("Quel est votre solde actuelle ? ")) != str or not solde.isdigit():
        print("Veuillez entrer un montant valide.")
    solde = float(solde)
    return solde

def ajouter_depense(solde, description, montant, historique):
    """Ajoute une dépense au solde."""
    solde += montant
    print(f"Votre nouvelle dépense de {montant} a été enregistrée. Nouveau solde : {solde}")
    historique.append(description)
    if solde < 0:
        print("Attention, votre solde est négatif, vous êtes à découvert !")
    return solde, historique

def ajouter_revenu(solde, description, montant, historique):
    """Ajoute un revenu au solde."""
    solde += montant
    print(f"Votre nouveau revenu de {montant} a été enregistré. Nouveau solde : {solde}")
    historique.append(description)
    return solde, historique

def afficher_solde(solde):  
    """Affiche le solde actuel."""
    print(f"Votre solde actuel est : {solde}")
    return solde

def afficher_historique(historique, solde):
    """Affiche l'historique des transactions."""
    if not historique:
        print("Aucune transaction enregistrée.")
    else:
        print("Historique des transactions :")
        for transaction in historique:
            print(f"- {transaction['date']}: {transaction['description']} de {transaction['montant']}")
