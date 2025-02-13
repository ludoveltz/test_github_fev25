# D'abord, nous devons avoir la classe Employee (classe parent)
class Employee:
    def __init__(self, firstname, lastname, age, job="employee", salary=5000):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary
    
    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"

# Ensuite, créer la classe Manager qui hérite d'Employee
class Manager(Employee):
    def __init__(self, firstname, lastname, age):
        # Appel du constructeur parent avec super()
        super().__init__(firstname, lastname, age, job="manager", salary=15000)
        self.employees = []  # Liste vide par défaut
    
    def add_new_employee(self, new_employee):
        self.employees.append(new_employee)
    
    def show_employees(self):
        if not self.employees:  # Si la liste est vide
            return f"{self.get_fullname()} n'a pas d'employés sous sa direction."
        
        result = f"Employés sous la direction de {self.get_fullname()}:"
        for employee in self.employees:
            result += f"\n- {employee.get_fullname()}"
        return result

# Création d'un objet Manager (Brad Pitt)
brad = Manager("Brad", "Pitt", 50)

# Affichage des attributs
print(f"Nom complet: {brad.get_fullname()}")
print(f"Âge: {brad.age}")
print(f"Poste: {brad.job}")
print(f"Salaire: {brad.salary}")

# Test 1 : Vérifier show_employees avec une liste vide
print("\n=== Test avec liste vide ===")
print(brad.show_employees())

# Test 2 : Créer et ajouter des employés
print("\n=== Ajout d'employés ===")
employee1 = Employee("John", "Doe", 30, "developer", 5000)
employee2 = Employee("Jane", "Smith", 28, "designer", 4500)
employee3 = Employee("Bob", "Johnson", 35, "analyst", 4800)

brad.add_new_employee(employee1)
brad.add_new_employee(employee2)
brad.add_new_employee(employee3)

# Test 3 : Vérifier show_employees avec la liste remplie
print("\n=== Liste des employés après ajout ===")
print(brad.show_employees())