# 1. Demander un nombre
nombre = input("Entrez un nombre entre 1 et 100 : ")

# 2. Convertir en nombre entier
nombre = int(nombre)

# 3. Vérifier les conditions FizzBuzz
if nombre % 3 == 0 and nombre % 5 == 0:
    print("FizzBuzz")
elif nombre % 3 == 0:
    print("Fizz")
elif nombre % 5 == 0:
    print("Buzz")
else:
    print(nombre)