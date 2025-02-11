# Liste des mots
words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']

# Création d'une nouvelle liste avec uniquement les mots en majuscules
uppercase_words = [word for word in words if word.isupper()]

# Afficher la nouvelle liste
print(uppercase_words)