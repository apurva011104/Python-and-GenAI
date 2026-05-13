import re

def validate_form_info(name: str, email: str, phone: str):
    try:
        if not re.match(r'^[A-Za-z]+$', name):
            raise ValueError("Invalid name")
    
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValueError("Invalid email")
    
        if not re.match(r'^\d{10}$', phone):
            raise ValueError("Invalid phone number")
        print("Valid inputs.")

    except ValueError as e:
        print(e)
    
name = input("Enter name: ")
email = input("Enter email: ")
phone = input("Enter phone number: ")

validate_form_info(name, email, phone)
