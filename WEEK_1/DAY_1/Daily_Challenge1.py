def create_multiples_list():
    try:
        # Demande à l'utilisateur d'entrer un nombre
        number = int(input("Enter a number: "))
        
        # Demande à l'utilisateur d'entrer la longueur souhaitée
        length = int(input("Enter the length: "))
        
        # Crée la liste des multiples en utilisant une compréhension de liste
        multiples = [number * i for i in range(1, length + 1)]
        
        # Affiche le résultat
        print(f"\nMultiples of {number} with length {length}:")
        print(multiples)
        
    except ValueError:
        print("Please enter valid numbers!")

# Test du programme
if __name__ == "__main__":
    create_multiples_list()