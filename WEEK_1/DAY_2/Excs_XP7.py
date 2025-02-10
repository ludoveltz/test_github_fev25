import random

def get_season_from_month(month):
    """Détermine la saison en fonction du numéro du mois."""
    if month in [12, 1, 2]:
        return 'winter'
    elif month in [3, 4, 5]:
        return 'spring'
    elif month in [6, 7, 8]:
        return 'summer'
    else:  # 9, 10, 11
        return 'autumn'

def get_random_temp(season):
    """Fonction qui retourne une température aléatoire (nombre à virgule) selon la saison."""
    if season.lower() == 'winter':
        return round(random.uniform(-10.0, 16.0), 1)
    elif season.lower() == 'spring':
        return round(random.uniform(5.0, 25.0), 1)
    elif season.lower() == 'summer':
        return round(random.uniform(20.0, 40.0), 1)
    elif season.lower() == 'autumn':
        return round(random.uniform(8.0, 22.0), 1)
    else:
        return "Saison non valide"

def main():
    """Fonction principale qui demande le mois et affiche la température avec des conseils."""
    # Demander le mois à l'utilisateur
    while True:
        try:
            month = int(input("Entrez le numéro du mois (1-12) : "))
            if 1 <= month <= 12:
                break
            print("Veuillez entrer un nombre entre 1 et 12 !")
        except ValueError:
            print("Veuillez entrer un nombre valide !")
    
    # Déterminer la saison
    season = get_season_from_month(month)
    
    # Obtenir la température aléatoire selon la saison
    temperature = get_random_temp(season)
    
    # Afficher la température
    print(f"\nPour le mois {month} (saison : {season})")
    print(f"La température actuelle est de {temperature} degrés Celsius.")
    
    # Donner des conseils en fonction de la température
    if temperature < 0:
        print("Brrr, il gèle ! Mettez plusieurs couches de vêtements aujourd'hui !")
    elif 0 <= temperature < 16:
        print("Il fait plutôt frais ! N'oubliez pas votre manteau !")
    elif 16 <= temperature < 23:
        print("La température est agréable, profitez-en pour sortir !")
    elif 23 <= temperature < 32:
        print("Il fait chaud, pensez à bien vous hydrater !")
    else:  # temperature >= 32
        print("Attention canicule ! Restez au frais et buvez beaucoup d'eau !")

# Exécution du programme
main()
