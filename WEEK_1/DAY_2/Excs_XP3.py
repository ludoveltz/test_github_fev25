brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

# Changement du nombre de magasins
brand["number_stores"] = 2

# Impression des clients de Zara
brand["number_stores"] = 2

# Impression des clients de Zara
print(f"Les clients de Zara sont : {', '.join(brand['type_of_clothes'])}")

# Ajout du pays de création 
brand["country_creation"] = "Spain"

# Vérification et ajout du concurrent 
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# Suppression de la date de création
del brand["creation_date"]

# Impression du dernier concurrent 
print(f"Dernier concurrent international : {brand['international_competitors'][-1]}")

# Impression des couleurs principales aux US
print(f"Couleurs principales aux US : {', '.join(brand['major_color']['US'])}")

# Nombre de paires clé-valeur
print(f"Nombre de paires clé-valeur : {len(brand)}")

# Impression des clés
print(f"Les clés du dictionnaire sont : {list(brand.keys())}")

# Création du nouveau dictionnaire
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

# Fusion des dictionnaires
brand.update(more_on_zara)

# Impression du nombre de magasins
print(f"Nombre de magasins : {brand['number_stores']}")

# La méthode update() a mis à jour la valeur de "number_stores" avec celle du nouveau dictionnaire more_on_zara. La valeur est passée de 2 à 10000 car les nouvelles valeurs écrasent les anciennes lors de la fusion des dictionnaires.