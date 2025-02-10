def make_shirt():
    """Fonction qui crée un t-shirt avec les entrées de l'utilisateur."""
    # Liste des tailles valides
    valid_sizes = ["XS", "S", "M", "L", "XL", "XXL"]
    
    # Demande de la taille
    while True:
        size = input("Entrez la taille du t-shirt (XS/S/M/L/XL/XXL) : ").upper()
        if size in valid_sizes:
            break
        else:
            print(f"Erreur : Taille invalide. Les tailles valides sont : {', '.join(valid_sizes)}")
    
    # Demande du texte
    text = input("Entrez le message à imprimer sur le t-shirt : ")
    
    # Affichage du résultat
    print(f"\nLa taille du t-shirt est {size} et le message est '{text}'")

# Lancement du programme
make_shirt()

def make_shirt(size="L", text="I love Python"):
    """Fonction qui crée un t-shirt avec une taille L et le message 'I love Python' par défaut."""
    print(f"\nLa taille du t-shirt est {size} et le message est '{text}'")

# Lancement du programme
make_shirt()

# 1. T-shirt large avec message par défaut
print("1. T-shirt large avec message par défaut :")
make_shirt()

# 2. T-shirt medium avec message par défaut
print("\n2. T-shirt medium avec message par défaut :")
make_shirt(size="M")

# 3. T-shirt de taille personnalisée avec message différent
print("\n3. T-shirt personnalisé :")
make_shirt("S", "J'aime coder")

# 4. Bonus - Utilisation des arguments nommés
print("\n4. Bonus - Arguments nommés :")
make_shirt(text="Python Forever", size="XL")