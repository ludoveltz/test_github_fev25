def chercher_index():
    # Définition de la liste (similaire à un array NumPy mais plus simple)
    names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
    
    try:
        # Demander le nom à l'utilisateur
        nom_recherche = input("Entrez un nom à rechercher : ")
        
        # Utiliser la méthode index() pour trouver la première occurrence
        # Similaire à np.where() dans NumPy, mais pour une liste simple
        index = names.index(nom_recherche)
        print(f"Le nom '{nom_recherche}' se trouve à l'index {index}")
        
    except ValueError:
        print(f"Le nom '{nom_recherche}' n'est pas dans la liste")

# Exécuter la fonction
chercher_index()
