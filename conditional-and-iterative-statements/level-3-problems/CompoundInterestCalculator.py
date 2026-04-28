principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate percentage: "))
years = int(input("Enter number of years: "))

for i in range(1,years+1,):
    principal = principal + (principal* (rate/100.0))
    print(f"Year {i}: {principal:.2f}")