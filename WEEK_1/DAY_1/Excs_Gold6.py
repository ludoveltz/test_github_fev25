import random

def jeu_devinettes():
    # Initialisation des compteurs
    victoires = 0
    defaites = 0
    
    print("Bienvenue au jeu de devinettes !")
    print("Devinez un nombre entre 1 et 9")
    print("Tapez '0' pour quitter\n")
    
    while True:
        try:
            # Demander le nombre à l'utilisateur
            choix_utilisateur = int(input("Votre nombre (1-9) : "))
            
            # Vérifier si l'utilisateur veut quitter
            if choix_utilisateur == 0:
                break
            
            # Valider l'entrée
            if choix_utilisateur < 1 or choix_utilisateur > 9:
                print("⚠️ Veuillez entrer un nombre entre 1 et 9")
                continue
            
            # Générer un nombre aléatoire
            nombre_aleatoire = random.randint(1, 9)
            
            # Vérifier la réponse
            if choix_utilisateur == nombre_aleatoire:
                print(f"🎉 Winner ! Le nombre était bien {nombre_aleatoire}")
                victoires += 1
            else:
                print(f"😔 Better luck next time. Le nombre était {nombre_aleatoire}")
                defaites += 1
                
        except ValueError:
            print("⚠️ Erreur : Veuillez entrer un nombre valide")
    
    # Afficher les statistiques finales
    total_parties = victoires + defaites
    if total_parties > 0:
        taux_victoire = (victoires / total_parties) * 100
        print("\n📊 Statistiques finales :")
        print(f"Parties jouées : {total_parties}")
        print(f"Victoires : {victoires}")
        print(f"Défaites : {defaites}")
        print(f"Taux de victoire : {taux_victoire:.1f}%")
    else:
        print("\nAucune partie jouée")

# Lancer le jeu
if __name__ == "__main__":
    jeu_devinettes()
