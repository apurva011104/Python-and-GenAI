employees = {
    "employee1":{"name":"Alexa","department":"HR","salary":"75000"},
    "employee2":{"name":"Alice","department":"Sales & Marketing","salary":"55000"},
    "employee3":{"name":"Ava","department":"IT","salary":"55000"},
    "employee4":{"name":"Annie","department":"Research & Development","salary":"45000"},
    "employee5":{"name":"Angel","department":"Customer Serice","salary":"45000"},
    "employee6":{"name":"Amy","department":"Operations","salary":"50000"}
}

for value in employees.values():
    if(float(value["salary"])>50000):
        print(value["name"])