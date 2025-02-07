# 1. Demander le nombre d'invités
nombre_invites = input("Combien d'invités seront présents à votre mariage ? ")

# 2. Convertir en nombre entier
nombre_invites = int(nombre_invites)

# 3. Déterminer le prix selon le nombre d'invités
if nombre_invites <= 50:
    prix = 4000
elif nombre_invites <= 100:
    prix = 10000
elif nombre_invites <= 200:
    prix = 15000
else:
    prix = 20000

# 4. Afficher le résultat
print(f"Pour {nombre_invites} invités, le prix du service traiteur sera de \${prix}")