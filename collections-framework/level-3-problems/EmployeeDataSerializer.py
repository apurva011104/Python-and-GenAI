import ast

input_string = input("Enter the list of employees with their department in format (name , department): ")

employee_list = ast.literal_eval(input_string)

json_list_of_employees = []

for emp in employee_list:
    dictionary = {}
    dictionary['name'] = emp[0]
    dictionary['department'] = emp[1]
    json_list_of_employees.append(dictionary)

print(json_list_of_employees)