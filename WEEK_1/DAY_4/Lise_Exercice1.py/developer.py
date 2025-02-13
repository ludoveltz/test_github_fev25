from employee import Employee

# Classe Developer qui hérite d'Employee
class Developer(Employee):
    def __init__(self, firstname, lastname, age):
        # Appel du constructeur parent avec les valeurs par défaut
        super().__init__(
            firstname=firstname,
            lastname=lastname,
            age=age,
            job="developer",  # Valeur par défaut pour job
            salary=15000      # Valeur par défaut pour salary
        )
        self.coding_skills = []  # Liste vide par défaut
    
    def add_skills(self, *skills):
        self.coding_skills.extend(skills)
    
    def coding(self):
        if self.coding_skills:
            return f"{self.get_fullname()} connaît les langages de programmation suivants : {', '.join(self.coding_skills)}"
        return f"{self.get_fullname()} ne connaît encore aucun langage de programmation"
    
    def coding_with_partner(self, other_developer):
        return f"{self.get_fullname()} et {other_developer.get_fullname()} programment ensemble.\n" \
               f"{self.firstname} connaît : {', '.join(self.coding_skills) if self.coding_skills else 'aucun langage'}\n" \
               f"{other_developer.firstname} connaît : {', '.join(other_developer.coding_skills) if other_developer.coding_skills else 'aucun langage'}"
    
    def get_promotion(self, promotion_amount):
        return super().get_promotion(promotion_amount)

# Test du code
# 1. Création des objets Developer
tom = Developer("Tom", "Cruiz", 30)
angelina = Developer("Angelina", "Jolie", 23)

# 2. Affichage des attributs initiaux
print("=== Attributs initiaux ===")
print(f"Developer 1: {tom.get_fullname()}, Age: {tom.age}, Job: {tom.job}, Salary: {tom.salary}€")
print(f"Developer 2: {angelina.get_fullname()}, Age: {angelina.age}, Job: {angelina.job}, Salary: {angelina.salary}€")

# 3. Test de la méthode add_skills
print("\n=== Test add_skills ===")
tom.add_skills("Python", "Java", "JavaScript")
angelina.add_skills("C++", "Ruby", "Python")

# 4. Test de la méthode coding
print("\n=== Test coding ===")
print(tom.coding())
print(angelina.coding())

# 5. Test de la méthode coding_with_partner
print("\n=== Test coding_with_partner ===")
print(tom.coding_with_partner(angelina))

# 6. Test de la méthode get_promotion
print("\n=== Test get_promotion ===")
print(f"Nouveau salaire de {tom.get_fullname()} après promotion (x2) : {tom.get_promotion(2)}€")
print(f"Nouveau salaire de {angelina.get_fullname()} après promotion (x1.5) : {angelina.get_promotion(1.5)}€")