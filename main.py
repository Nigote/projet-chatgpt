user_name = input("Quelle est votre nom ? ")
print(f"Bonjour, {user_name}, bienvenue!")
solde = int(input("Quel est votre solde actuel ? "))
while True :
    menu = input("""Que voulez vous faire ?:
                 1-Ajouter une dépense
                 2-Ajouter un revenu
                 3-Voir le solde
                 0-Quitter
                 """)
    if menu == '1':
        depense = float(input("Entrez le montant de la dépense : "))
        solde -= depense
        print(f"Votre nouveau solde est : {solde}")
    elif menu == '2':
        revenu = float(input("Entrez le montant du revenu : "))
        solde += revenu
        print(f"Votre nouveau solde est : {solde}")
    elif menu == '3':
        print(f"Votre solde actuel est : {solde}")
    elif menu == '0':
        print("Merci d'avoir utilisé notre service. Au revoir!")
        break
    else :
        print("Option invalide, veuillez réessayer.")
        