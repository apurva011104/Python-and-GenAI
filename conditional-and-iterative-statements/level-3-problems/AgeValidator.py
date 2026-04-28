inp = input("Enter list of customer's age: ")

customersAge = inp.replace(" ","")[1:-1].split(",")

count = 0

for age in customersAge:
    if int(age) > 18:
        count+=1

print(f"Number of customers above 18: {count}")