class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print(f'{self.brand} {self.model} is driving!')

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def drive(self):
        print(f'{self.brand} {self.model} with {self.battery_size}kWh battery is driving silently!')

if __name__ == "__main__":
    my_electric_car = ElectricCar('Tesla', 'Model S', 100)
    my_electric_car.drive()