# Parent class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# First Child class
class Engine(Car):
    def __init__(self, make, model, year, horsepower):
        Car.__init__(self, make, model, year)
        self.horsepower = horsepower
    
    def display_info(self):
        return f"{Car.display_info(self)}, {self.horsepower}HP"

# Second Child Class
class Wheel(Car):
    def __init__(self, make, model, year, size):
        Car.__init__(self, make, model, year)
        self.size = size
    
    def display_info(self):
        return f"{Car.display_info(self)}, {self.size} inch wheels"

my_car = Car("Hyundai", "Santro", 2010)
my_engine = Engine("Hyundai", "Santro", 2010, 50)
my_wheel = Wheel("Hyundai", "Santro", 2010, 14)

print(my_car.display_info())
print(my_engine.display_info())
print(my_wheel.display_info())
