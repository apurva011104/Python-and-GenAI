def calculate_net_salary( gross: float , tax_rate: float ):
    tax = (gross * tax_rate) / 100.0
    return gross - tax

gross = float(input("Enter gross salary: "))
tax_rate = float(input("Enter tax rate: "))

net_salary = calculate_net_salary(gross, tax_rate)

print(net_salary)