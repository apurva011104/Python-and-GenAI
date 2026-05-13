class Temperature:
    def to_celsius(self, f: float):
        return (f - 32) * 5 / 9

    def to_fahrenheit(self, c: float):
        return (c * 9 / 5) + 32


t = Temperature()
temp_in_celsius = float(input("Enter temperature in Celsius: "))
print(f"Temperature in Fahrenheit: {t.to_fahrenheit(temp_in_celsius)}")

temp_in_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
print(f"Temperature in Celsius: {t.to_celsius(temp_in_fahrenheit)}")
