class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_details(self):
        return f"Name:{self.name}\nAge:{self.age}\nSalary':{self.salary}"

class Manager(Employee):
    def __init__(self, name, age, salary,department):
        super().__init__(name, age, salary)
        self.department = department
    
    def get_details(self):
        return f"{super().get_details()}\nDepartment:{self.department}"
    
class Engineer(Employee):
    def __init__(self, name, age, salary,skill):
        super().__init__(name, age, salary)
        self.skill = skill
    
    def get_details(self):
        return f"{super().get_details()}\nDSkill:{self.skill}"
    

manager = Manager("james",25,4500,"AI")
print(manager.get_details())

engi = Engineer("james",25,4500,"Python")
print(engi.get_details())