# Classe de base Employee
class Employee:
    def __init__(self, firstname, lastname, age, job=None, salary=0):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary
    
    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"
    
    def get_promotion(self, promotion_amount):
        self.salary *= promotion_amount  # Multiplication pour la cohérence
        return self.salary