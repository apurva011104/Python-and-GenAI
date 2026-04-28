departments = [("IT", 10), ("HR", 5), ("Finance", 8)]

totalEmployees = 0

for dept in departments:
    totalEmployees += dept[1]

print(f"Departments: {departments}")
print(f"Total Employees: {totalEmployees}")