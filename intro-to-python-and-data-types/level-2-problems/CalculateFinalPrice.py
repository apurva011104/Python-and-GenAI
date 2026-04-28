name=input("Enter product name: ")
price=float(input("Enter product price: "))
discount=float(input("Enter product discount: "))

finalPrice = price - ((price * discount) / 100.0)

print(f"Product details:[Name: {name}, Price: {price:.2f}INR, Discount: {discount:.2f}%, Final Price: {finalPrice:.2f}INR]")