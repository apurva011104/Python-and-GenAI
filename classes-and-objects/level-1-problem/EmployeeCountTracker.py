import ast

class Employee:
    count = 0

    def __init__(self, name: str):
        self.name = name
        Employee.count += 1


employee_list_string = input("Enter list of employee's names: ")

employee_list = ast.literal_eval(employee_list_string)

for i in employee_list:
    e = Employee(i)

print(Employee.count)