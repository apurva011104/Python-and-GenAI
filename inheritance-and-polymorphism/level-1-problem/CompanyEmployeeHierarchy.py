class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name: str, salary: float, bonus: float):
        super().__init__(name, salary)
        self.bonus = bonus

    def total_salary(self):
        return self.salary + self.bonus


m = Manager("Riya", 60000, 10000)
print(m.total_salary())