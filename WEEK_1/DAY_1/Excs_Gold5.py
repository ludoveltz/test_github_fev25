def trouver_plus_grand_nombre():
    try:
        # Collecte des nombres
        nombre1 = float(input("Entrez le 1er nombre : "))
        nombre2 = float(input("Entrez le 2ème nombre : "))
        nombre3 = float(input("Entrez le 3ème nombre : "))
        
        # Méthode 1 : Utilisation de max() native
        plus_grand = max(nombre1, nombre2, nombre3)
        
        # Affichage du résultat
        print(f"\nLe plus grand nombre est : {plus_grand}")
        
        # Bonus : Approche style NumPy (pour votre formation en ML)
        nombres = [nombre1, nombre2, nombre3]
        print(f"Index du plus grand nombre : {nombres.index(plus_grand)}")
        
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides")

# Exécution du programme
trouver_plus_grand_nombre()
