def verifier_nom():
    # Définir le nom recherché
    mon_nom = "Ludo"
    
    # Initialiser la boucle
    while True:
        # Demander le nom à l'utilisateur
        nom_saisi = input("Entrez un nom (ou 'q' pour quitter) : ")
        
        # Option pour quitter proprement
        if nom_saisi.lower() == 'q':
            print("Au revoir !")
            break
            
        # Vérifier si le nom correspond
        if nom_saisi == mon_nom:
            print(f"Bonjour {mon_nom} ! C'est bien vous !")
            break
        else:
            print("Ce n'est pas le bon nom, essayez encore.")

# Exécuter la fonction
verifier_nom()
