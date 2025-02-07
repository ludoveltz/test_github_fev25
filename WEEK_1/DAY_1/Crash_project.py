import random

def number_guessing_game():
    # Générer un nombre aléatoire entre 1 et 100
    random_number = random.randint(1, 100)
    max_attempts = 7

    print("🎮 Welcome in number guessing game !")
    print(f"Tu as {max_attempts} tentatives pour deviner le nombre entre 1 et 100")

    # Boucle pour les tentatives
    for attempt in range(max_attempts):
        # Demander et vérifier l'entrée de l'utilisateur
        try:
            guess = int(input(f"\nattempt {attempt + 1}/{max_attempts}. Ton nombre ? "))

            # Vérifier si le nombre est correct
            if guess < random_number:
                print("📈 Too low !")
            elif guess > random_number:
                print("📉 Too high !")
            else:
                print(f"🎉 Félicitations ! Tu as trouvé le nombre {random_number} !")
                break

        except ValueError:
            print("⚠️ Entre un nombre valide !")
            continue

    print(f"\n❌ Game Over ! Le nombre était {random_number}")

# Lancer le jeu
number_guessing_game()