# # constructor
# class Person:
#     name="something"
#     age=12
#     gender="male"

#     def __init__(self, ):
#         print("Person")

# person=Person()

# print(person.name)


class House:
    # attributes
    door = 10
    window = 5
    color = "red"

# magic method
# constuctor, str method, comparison method
    def __init__(self, door, window, color):
        self.door = door
        self.window = window
        self.color = color

    def __str__(self):
        return self.color

ram_ko_ghar=House(door=2,window=1, color="green")

print(ram_ko_ghar.color)

# print(ram_ko_ghar.window)
# print(ram_ko_ghar.door)

# hari_ko_ghar=House(door=5,window=4, color="black")
# print(hari_ko_ghar.color)
# print(hari_ko_ghar.window)
# print(hari_ko_ghar.door)

print("\nComparison Method\n")

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __eq__ (self, object):
        return self.salary == object.salary
    
    def __gt__ (self, object):
        return self.salary > object.salary
    
    def __le__ (self, object):
        return self.age <= object.age

ram = Employee("ram", 22, 2000)
shyam = Employee("shyam", 22, 2200)

print(ram <= shyam)


# inheritance
# parent class.....child class
print("\nInheritance\n")

class Grandfather:
    house = "Luxury House"

class Father(Grandfather):
    car = "Lamborghini"

class Mother:
    jewellery = "Diamond"

class Son(Father, Mother):
    console = "PS5"


son = Son()
print(son.console)
print(son.car)
print(son.house)
print(son.jewellery)
# print(father.console)

# father = Father()
# print(father.console)
# son = Son()
# print(son.jewellery)

print("\nInheritance Second Example\n")

# Parent class (superclass)
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# Child class (subclass) inheriting from Car
class Engine(Car):
    def __init__(self, make, model, year, horsepower):
        super().__init__(make, model, year)
        self.horsepower = horsepower
    
    def display_info(self):
        return f"{super().display_info()}, {self.horsepower}HP"

# Another child class (subclass) inheriting from Car
class Wheel(Car):
    def __init__(self, make, model, year, size):
        super().__init__(make, model, year)
        self.size = size
    
    def display_info(self):
        return f"{super().display_info()}, {self.size} inch wheels"

# Creating instances of the classes
my_car = Car("Hyundai", "Santro", 2010)
my_engine = Engine("Hyundai", "Santro", 2010, 50)
my_wheel = Wheel("Hyundai", "Santro", 2010, 14)

# Using the methods
print(my_car.display_info())    # Output: 2023 Toyota Camry
print(my_engine.display_info()) # Output: 2023 Toyota Camry, 203HP
print(my_wheel.display_info())  # Output: 2023 Toyota Camry, 18 inch wheels
