# Oui, la classe Farm a besoin d'une méthode __init__.
# L'__init__ devrait prendre au moins un paramètre : le nom de la ferme.

class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

# la méthode add_animal utilise un paramètre par défaut pour le nombre d'animaux.
# ce qui permet d'appeler la méthode avec un seul argument lorsque vous ajoutez un seul animal.

    def add_animal(self, animal, count=1):
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def get_info(self):
        info = f"{self.name}'s farm\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_list = ', '.join(animal_types[:-1]) + ' and ' + animal_types[-1] + 's'
        return f"{self.name}'s farm has {animal_list}."

# Création de l'objet Farm et ajout des animaux
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

# Affichage des informations de la ferme
print(macdonald.get_info())

# Bonus : obtenir la liste des types d'animaux et une description courte
print(macdonald.get_animal_types())
print(macdonald.get_short_info())