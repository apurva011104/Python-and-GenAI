from collections import defaultdict
import ast

department_employees_input = input("Enter (department, employee) list: ")

department_employees_input = department_employees_input.replace("[","").replace("]","")

employees_list = ast.literal_eval(department_employees_input)

#employees_list = list(employees_list)

departments_dict = defaultdict(list)

for cat, item in employees_list:
    departments_dict[cat].append(item)

print(dict(departments_dict))