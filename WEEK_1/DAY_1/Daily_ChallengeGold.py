from datetime import datetime

def dessiner_gateau(nombre_bougies, est_annee_bissextile=False):
    """
    Dessine un gâteau ASCII avec le nombre spécifié de bougies
    """
    # Construction des bougies
    bougies = "i" * nombre_bougies
    espace_bougies = "_" * ((11 - len(bougies)) // 2)
    ligne_bougies = f"       {espace_bougies}{bougies}{espace_bougies}"
    
    # Structure du gâteau
    gateau = [
        ligne_bougies,
        "      |:H:a:p:p:y:|",
        "    __|___________|__",
        "   |^^^^^^^^^^^^^^^^^|",
        "   |:B:i:r:t:h:d:a:y:|",
        "   |                 |",
        "   ~~~~~~~~~~~~~~~~~~~"
    ]
    
    # Afficher le gâteau
    for ligne in gateau:
        print(ligne)
    
    # Si c'est une année bissextile, afficher un deuxième gâteau
    if est_annee_bissextile:
        print("\nBonus : Année bissextile = Double gâteau !")
        print()
        for ligne in gateau:
            print(ligne)

def verifier_annee_bissextile(annee):
    """
    Vérifie si une année est bissextile
    """
    return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)

def calculer_age_et_gateau():
    """
    Fonction principale qui gère l'interaction avec l'utilisateur
    """
    while True:
        try:
            # Demander la date de naissance
            print("Entrez votre date de naissance (format: JJ/MM/AAAA)")
            date_naissance = input("> ")
            
            # Convertir la date
            date_obj = datetime.strptime(date_naissance, "%d/%m/%Y")
            
            # Calculer l'âge
            aujourd_hui = datetime.now()
            age = aujourd_hui.year - date_obj.year
            
            # Ajuster l'âge si l'anniversaire n'est pas encore passé cette année
            if aujourd_hui.month < date_obj.month or \
               (aujourd_hui.month == date_obj.month and aujourd_hui.day < date_obj.day):
                age -= 1
            
            # Obtenir le dernier chiffre de l'âge pour les bougies
            nombre_bougies = age % 10
            
            # Vérifier si c'est une année bissextile
            est_bissextile = verifier_annee_bissextile(date_obj.year)
            
            # Afficher les résultats
            print(f"\nVous avez {age} ans !")
            if est_bissextile:
                print("Vous êtes né(e) une année bissextile !")
            
            # Dessiner le(s) gâteau(x)
            dessiner_gateau(nombre_bougies, est_bissextile)
            break
            
        except ValueError:
            print("⚠️ Format de date incorrect. Utilisez JJ/MM/AAAA")
            
if __name__ == "__main__":
    calculer_age_et_gateau()
