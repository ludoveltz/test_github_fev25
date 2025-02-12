# Classes existantes
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 1. Création de la nouvelle race Siamese
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 2. Création des instances de chats et de la liste all_cats
bengal_cat = Bengal("Leo", 3)
chartreux_cat = Chartreux("Felix", 5)
siamese_cat = Siamese("Luna", 2)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# 3. Création de l'instance Pets pour Sara
sara_pets = Pets(all_cats)

# 4. Faire marcher tous les chats
sara_pets.walk()