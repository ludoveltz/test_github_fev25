def creer_matrice():
    """Création de la matrice à partir des données"""
    return [
        ['7', 'i', 'i'],
        ['T', 's', 'x'],
        ['h', '%', '?'],
        ['i', ' ', '#'],
        ['s', 'M', ' '],
        ['\$', 'a', ' '],
        ['#', 't', '%'],
        ['^', 'r', '!']
    ]

def est_alpha(caractere):
    """Vérifie si un caractère est alphabétique"""
    return caractere.isalpha()

def decoder_matrice(matrice):
    """Décode le message caché dans la matrice"""
    nb_lignes = len(matrice)
    nb_colonnes = len(matrice[0])
    message = []
    dernier_etait_alpha = False
    
    # Parcourir chaque colonne
    for colonne in range(nb_colonnes):
        for ligne in range(nb_lignes):
            caractere = matrice[ligne][colonne]
            
            if est_alpha(caractere):
                # Si c'est une lettre, l'ajouter au message
                message.append(caractere)
                dernier_etait_alpha = True
            elif dernier_etait_alpha:
                # Si c'est un symbole après une lettre, ajouter un espace
                if message[-1] != ' ':
                    message.append(' ')
                dernier_etait_alpha = False
    
    # Nettoyer les espaces en trop
    message_final = ''.join(message).strip()
    while '  ' in message_final:
        message_final = message_final.replace('  ', ' ')
    
    return message_final

def afficher_matrice(matrice):
    """Affiche la matrice de façon lisible"""
    print("\nMatrice originale :")
    for ligne in matrice:
        print(' '.join(ligne))

def main():
    # Création et affichage de la matrice
    matrice = creer_matrice()
    afficher_matrice(matrice)
    
    # Décodage et affichage du message
    message = decoder_matrice(matrice)
    print("\nMessage décodé :")
    print(message)

if __name__ == "__main__":
    main()
