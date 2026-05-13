class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department


class Manager(Employee):
    def __init__(self, name, department, team_size):
        super().__init__(name, department)
        self.team_size = team_size

    def display(self):
        print(f"Manager: {self.name} | Department: {self.department} | Team Size: {self.team_size}")


m = Manager("Alex", "IT", 10)
m.display()