try:
    dividend = float(input("Enter dividend: "))
    divisor = float(input("Enter divisor: "))
    result = dividend / divisor
    print(result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input type.")