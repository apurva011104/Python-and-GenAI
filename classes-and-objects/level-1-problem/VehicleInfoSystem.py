class Vehicle:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


car_name = input("Enter the brand of the vehicle: ")
car_model = input("Enter the model of the vehicle: ")
v = Vehicle(car_name, car_model)
v.display()