taxRate = 15.0
costPrice = float(input("Enter cost price of product: "))
sellingPrice = costPrice + ((taxRate*costPrice)/100.0)

print(f"Selling Price: {sellingPrice:.2f}INR")