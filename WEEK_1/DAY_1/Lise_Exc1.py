# 1. Demander le nombre de miles
miles = input("Entrez le nombre de miles à convertir : ")

# 2. Convertir en float
miles = float(miles)

# 3. Faire la conversion 
kilometres = miles * 1.60934

# 4. Afficher avec 2 décimales
print(f"{miles} miles équivaut à {kilometres:.2f} kilomètres")