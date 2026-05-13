class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand: str, model: str):
        super().__init__(brand)
        self.model = model


class ElectricCar(Car):
    def __init__(self, brand: str, model: str, battery: float):
        super().__init__(brand, model)
        self.battery = battery

    def display(self):
        print(f"Brand: {self.brand} | Model: {self.model} | Battery: {self.battery}%")


ec = ElectricCar("Tesla", "Model X", 90)
ec.display()