# Première partie : Afficher tous les nombres de 1 à 20
print("Partie 1 : Tous les nombres de 1 à 20")
for nombre in range(1, 21):  # 21 car range s'arrête avant la dernière valeur
    print(nombre, end=" ")  # end=" " pour afficher sur une même ligne

# Saut de ligne pour séparer les deux parties
print("\n")

# Deuxième partie : Afficher les nombres avec un index pair
print("Partie 2 : Nombres avec index pair")
for index in range(1, 21):
    if index % 2 == 0:  # Vérifie si l'index est pair
        print(index, end=" ")

print()  # Saut de ligne final
