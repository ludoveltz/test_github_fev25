# 1. Demander les trois nombres
nombre1 = input("Entrez le premier nombre : ")
nombre2 = input("Entrez le deuxième nombre : ")
nombre3 = input("Entrez le troisième nombre : ")

# 2. Trouver le plus grand nombre avec if/else
if nombre1 >= nombre2 and nombre1 >= nombre3:
    plus_grand = nombre1
elif nombre2 >= nombre1 and nombre2 >= nombre3:
    plus_grand = nombre2
else:
    plus_grand = nombre3

# 3. Afficher le résultat
print(f"Le plus grand nombre est : {plus_grand}")