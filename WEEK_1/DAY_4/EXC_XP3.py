# First, we need the Dog class from the previous exercise
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight/self.age * 10

    def fight(self, other_dog):
        my_score = self.run_speed() * self.weight
        other_score = other_dog.run_speed() * other_dog.weight
        winner = self.name if my_score > other_score else other_dog.name
        return f"{winner} won the fight"

# Now, let's create the PetDog class that inherits from Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        # Call the parent class's __init__ method
        super().__init__(name, age, weight)
        # Add the trained attribute
        self.trained = False

    def train(self):
        # Print bark output and set trained to True
        print(self.bark())
        self.trained = True
        return self

    def play(self, *args):
        # Create list of all dog names including self
        all_dogs = [self.name] + [dog.name for dog in args]
        # Join names with commas and 'and' for the last one
        dogs_string = ", ".join(all_dogs[:-1]) + f" and {all_dogs[-1]}"
        print(f"{dogs_string} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet!")

# Test the implementation
if __name__ == "__main__":
    # Create some pet dogs
    pet1 = PetDog("Rex", 4, 30)
    pet2 = PetDog("Buddy", 2, 15)
    pet3 = PetDog("Luna", 3, 20)

    # Test 1: Try to do a trick before training
    print("Test 1: Untrained trick attempt")
    pet1.do_a_trick()

    # Test 2: Train the dog and try a trick
    print("\nTest 2: Training and trick")
    pet1.train()
    pet1.do_a_trick()

    # Test 3: Play together
    print("\nTest 3: Playing together")
    pet1.play(pet2, pet3)

    # Test 4: Multiple tricks after training
    print("\nTest 4: Multiple tricks")
    pet1.do_a_trick()
    pet1.do_a_trick()
