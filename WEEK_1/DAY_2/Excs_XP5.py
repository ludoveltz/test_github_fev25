import random

def compare_numbers():
    #Fonction qui compare un nombre entré par l'utilisateur avec un nombre aléatoire
    try:
        # Demande à l'utilisateur d'entrer un nombre
        user_input = input("Veuillez entrer un nombre entre 1 et 100 : ")
        user_number = int(user_input)
        
        # Vérifie si le nombre est dans la plage valide
        if not 1 <= user_number <= 100:
            print("Erreur : Le nombre doit être entre 1 et 100")
            return
        
        # Génère un nombre aléatoire
        random_number = random.randint(1, 100)
        
        # Compare les nombres
        if user_number == random_number:
            print(f"🎉 Félicitations ! Les deux nombres sont {user_number}")
        else:
            print(f"❌ Pas de chance !")
            print(f"Votre nombre était : {user_number}")
            print(f"Le nombre aléatoire était : {random_number}")
            
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide")

# Lancement du jeu
compare_numbers()
