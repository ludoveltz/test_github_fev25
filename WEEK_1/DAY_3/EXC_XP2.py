class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Créer l'objet davids_dog
davids_dog = Dog("Rex", 50)

# Afficher les détails du chien de David et appeler les méthodes
print(f"David's dog is named {davids_dog.name} and is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

# Créer l'objet sarahs_dog
sarahs_dog = Dog("Teacup", 20)

# Afficher les détails du chien de Sarah et appeler les méthodes
print(f"Sarah's dog is named {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

# Vérifier quel chien est plus grand
if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
else:
    print(f"The bigger dog is {sarahs_dog.name}.")
