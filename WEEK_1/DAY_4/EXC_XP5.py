# First, create the base Family class
class Family:
    def __init__(self, last_name, members):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        # Add is_child flag automatically
        kwargs['is_child'] = True
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family! Welcome to {kwargs['name']}!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"\nFamily {self.last_name} members:")
        for member in self.members:
            print("\nMember Details:")
            for key, value in member.items():
                print(f"{key}: {value}")

# Create TheIncredibles class inheriting from Family
class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if self.is_18(name):
                    print(f"{member['incredible_name']}'s power is: {member['power']}")
                else:
                    raise Exception(f"{name} is not over 18 years old!")

    def incredible_presentation(self):
        print(f"\n* Here is our powerful family - The {self.last_name} *")
        super().family_presentation()

# Test the implementation
if __name__ == "__main__":
    # Create initial members
    initial_members = [
        {'name':'Michael','age':35,'gender':'Male','is_child':False,
         'power':'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,
         'power':'read minds','incredible_name':'SuperWoman'}
    ]

    # Create an instance of TheIncredibles
    incredibles = TheIncredibles("Incredibles", initial_members)

    # Test 1: Initial presentation
    print("Initial Family Status:")
    incredibles.incredible_presentation()

    # Test 2: Use powers
    print("\nTesting powers:")
    try:
        incredibles.use_power("Michael")
        incredibles.use_power("Sarah")
    except Exception as e:
        print(f"Error: {e}")

    # Test 3: Add Baby Jack
    print("\nAdding Baby Jack to the family:")
    incredibles.born(
        name="Jack",
        age=0,
        gender="Male",
        power="Unknown Power",
        incredible_name="BabyJack"
    )

    # Test 4: Final presentation
    print("\nUpdated Family Status:")
    incredibles.incredible_presentation()

    # Test 5: Try to use baby's power (should raise an exception)
    print("\nTrying to use Baby Jack's power:")
    try:
        incredibles.use_power("Jack")
    except Exception as e:
        print(f"Error: {e}")