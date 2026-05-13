import re

text = input("Enter the text: ")

if re.match(r'^[A-Z]', text):
    print("Starts with a capital letter")
else:
    print("Does not starts with a capital letter")