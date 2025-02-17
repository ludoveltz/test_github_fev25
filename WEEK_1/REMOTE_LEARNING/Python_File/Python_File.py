# Il faut utiliser le chemin complet du fichier
file_path = '/Users/ludovicveltz/Documents/Bootcamp_GENAI_2025/Crashcourse/WEEK_1/REMOTE_LEARNING/Python_File/nameslist.txt'

# 1. Lire le fichier ligne par ligne
with open(file_path, 'r') as file:
    for line in file:
        print(line)

# 2. Lire uniquement la 5ème ligne
with open(file_path, 'r') as file:
    fifth_line = file.readlines()[4]  # l'index commence à 0

# 3. Lire les 5 premiers caractères
with open(file_path, 'r') as file:
    first_five = file.read(5)

# 4. Lire tout le fichier et le retourner comme liste de strings
with open(file_path, 'r') as file:
    content = file.read()
    words = content.split()

# 5. Compter les occurrences
with open(file_path, 'r') as file:
    content = file.read()
    darth_count = content.count('Darth')
    luke_count = content.count('Luke')
    lea_count = content.count('Lea')

# 6. Ajouter votre prénom à la fin
with open(file_path, 'a') as file:
    file.write('\nLudovic')

# 7. Ajouter "Skywalker" après chaque "Luke"
with open(file_path, 'r') as file:
    content = file.read()
content_modified = content.replace('Luke', 'Skywalker')
with open(file_path, 'w') as file:
    file.write(content_modified)
