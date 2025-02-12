class Family:
    def __init__(self, last_name, members):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        """Add a new child to the family"""
        # Add is_child flag automatically
        kwargs['is_child'] = True
        # Add the new member to the family
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family! "
              f"Welcome to {kwargs['name']}!")

    def is_18(self, name):
        """Check if a family member is over 18"""
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False  # Return False if name not found

    def family_presentation(self):
        """Present the entire family"""
        print(f"\nFamily {self.last_name} members:")
        for member in self.members:
            print("\nMember Details:")
            for key, value in member.items():
                print(f"{key}: {value}")

# Test the implementation
if __name__ == "__main__":
    # Create initial members list
    initial_members = [
        {'name':'Michael','age':35,'gender':'Male','is_child':False},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False}
    ]

    # Create a family instance
    smith_family = Family("Smith", initial_members)

    # Test family_presentation method
    print("Initial Family Presentation:")
    smith_family.family_presentation()

    # Test born method
    print("\nAdding a new baby to the family:")
    smith_family.born(name="Emma", age=0, gender="Female")

    # Test is_18 method
    print("\nChecking ages:")
    for member in smith_family.members:
        name = member['name']
        is_adult = smith_family.is_18(name)
        print(f"Is {name} over 18? {is_adult}")

    # Show final family presentation
    print("\nFinal Family Presentation:")
    smith_family.family_presentation()