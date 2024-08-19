class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print(f'{self.brand} {self.model} is driving!')

if __name__ == "__main__":
    my_car = Car('Toyota', 'Corolla')
    my_car.drive()