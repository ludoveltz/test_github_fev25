family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

# Vérification du prix pour chaque membre
for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
        
    print(f"{name} doit payer $${price}")
    total_cost += price

print(f"\nLe coût total pour la famille est : $${total_cost}")

def get_ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else:
        return 15

# Création d'un dictionnaire vide
family = {}

# Demande à l'utilisateur d'entrer les informations
while True:
    name = input("Entrez le nom (ou 'quit' pour terminer) : ")
    if name.lower() == 'quit':
        break
        
    try:
        age = int(input("Entrez l'âge : "))
        family[name] = age
    except ValueError:
        print("Veuillez entrer un âge valide")
        continue

# Calcul des prix
total_cost = 0
for name, age in family.items():
    price = get_ticket_price(age)
    print(f"{name} doit payer $${price}")
    total_cost += price

print(f"\nLe coût total pour la famille est : $${total_cost}")
