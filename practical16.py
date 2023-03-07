class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")


class Qualification:
    def __init__(self, degree, specialization, university):
        self.degree = degree
        self.specialization = specialization
        self.university = university
    def display_details(self):
        print(f"Degree: {self.degree}")
        print(f"Specialization: {self.specialization}")
        print(f"University: {self.university}")


class Scientist(Employee, Qualification):
    def __init__(self, name, employee_id, salary, degree, specialization, 
        university, research_area):
        Employee.__init__(self, name, employee_id, salary)
        Qualification.__init__(self, degree, specialization, university)
        self.research_area = research_area
    def display_details(self):
        Employee.display_details(self)
        Qualification.display_details(self)
        print(f"Research Area: {self.research_area}")


class Manager(Employee, Qualification):
    def __init__(self, name, employee_id, salary, degree, specialization, 
        university, department):
        Employee.__init__(self, name, employee_id, salary)
        Qualification.__init__(self, degree, specialization, university)
        self.department = department
    def display_details(self):
        Employee.display_details(self)
        Qualification.display_details(self)
        print(f"Department: {self.department}")


scientist = Scientist("Deepak Kumar", "190303105339", 90000, "PhD", 
"Computer Science", "Parul University", "Artificial Intelligence")
scientist.display_details()
manager = Manager("Vinu", "19033105591", 70000, "MBA", "Finance", "Parul University", "Sales")
manager.display_details()