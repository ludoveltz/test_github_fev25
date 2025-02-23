import numpy as np

# 1. Création des tableaux
# Tableau 1D de 1 à 5
array_1d = np.arange(1, 6)  # arange crée un tableau de 1 (inclus) à 6 (exclus)
print("Tableau 1D:")
print(array_1d)

# Tableau 2D de 1 à 6, reshape en 2x3
array_2d = np.arange(1, 7).reshape(2, 3)  # reshape réorganise en 2 lignes et 3 colonnes
print("\nTableau 2D:")
print(array_2d)

# 2. Inspection des attributs
print("\nAttributs du tableau 1D:")
print("Shape:", array_1d.shape)
print("Size:", array_1d.size)
print("Type de données:", array_1d.dtype)

print("\nAttributs du tableau 2D:")
print("Shape:", array_2d.shape)
print("Size:", array_2d.size)
print("Type de données:", array_2d.dtype)

# 3. Création d'un tableau avec type de données spécifique
array_float = np.array([1, 2, 3], dtype=float)
print("\nTableau avec type float:")
print(array_float)
print("Type de données:", array_float.dtype)
