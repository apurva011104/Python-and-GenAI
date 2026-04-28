employees = {
    "employee1":{"id":"101","name":"Alexa","salary":"75000"},
    "employee2":{"id":"102","name":"Alice","salary":"55000"},
    "employee3":{"id":"103","name":"Ava","salary":"55000"},
    "employee4":{"id":"104","name":"Annie","salary":"45000"},
    "employee5":{"id":"105","name":"Angel","salary":"45000"},
    "employee6":{"id":"106","name":"Amy","salary":"50000"}
}

idToSearch = input("Enter employee id to retrieve information: ")

foundEmp = {}

for emp in employees.values():
    if(emp["id"]==idToSearch):
        foundEmp = emp
        break

if(len(foundEmp)==0):
    print("Employee Not Found")
else:
    print(emp)