class Employee:
    def __init__(self, firstname, lastname, age, job, salary):
        """Initialize Employee attributes"""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary
    
    def get_fullname(self):
        """Return the full name of the employee"""
        return f"{self.firstname} {self.lastname}"
    
    def happy_birthday(self):
        """Increment age by one and return new age"""
        self.age += 1
        return self.age
    
    def get_promotion(self, promotion_amount):
        """Increment salary by promotion amount"""
        self.salary += promotion_amount
        return self.salary
    
    def show_info(self):
        """Display all information about the employee"""
        print(f"Name: {self.get_fullname()}")
        print(f"Age: {self.age}")
        print(f"Job: {self.job}")
        print(f"Salary: {self.salary} euros")
        print("-" * 30)

# Creating employee objects
employee1 = Employee("Lea", "Smith", 30, "developer", 25000)
employee2 = Employee("David", "Schartz", 20, "project manager", 20000)

# Displaying initial information
print("Initial Information:")
employee1.show_info()
employee2.show_info()

# Testing get_fullname method
print("Full Names:")
print(f"Employee 1: {employee1.get_fullname()}")
print(f"Employee 2: {employee2.get_fullname()}")
print("-" * 30)

# Testing happy_birthday method
print("After Birthday:")
print(f"{employee1.get_fullname()}'s new age: {employee1.happy_birthday()}")
print(f"{employee2.get_fullname()}'s new age: {employee2.happy_birthday()}")
print("-" * 30)

# Testing get_promotion method
print("After Promotion:")
print(f"{employee1.get_fullname()}'s new salary: {employee1.get_promotion(5000)} euros")
print(f"{employee2.get_fullname()}'s new salary: {employee2.get_promotion(3000)} euros")
print("-" * 30)

# Showing final information
print("Final Information:")
employee1.show_info()
employee2.show_info()