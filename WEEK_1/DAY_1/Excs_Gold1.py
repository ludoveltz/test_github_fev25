def determiner_saison():
    try:
        # Demander à l'utilisateur d'entrer un mois
        mois = int(input("Entrez un numéro de mois (1 à 12) : "))
        
        # Vérifier si le mois est valide
        if mois < 1 or mois > 12:
            return "Erreur : Veuillez entrer un nombre entre 1 et 12."
        
        # Déterminer la saison
        if 3 <= mois <= 5:
            saison = "Printemps"
        elif 6 <= mois <= 8:
            saison = "Été"
        elif 9 <= mois <= 11:
            saison = "Automne"
        else:  # mois 12, 1, 2
            saison = "Hiver"
            
        return f"Le mois {mois} est en {saison}."
    
    except ValueError:
        return "Erreur : Veuillez entrer un nombre valide."

# Exécution du programme
print(determiner_saison())
