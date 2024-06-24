print("\nInheritance\n")

class Grandfather:
    house = "Luxury House"

    def __init__(self) -> None:
        print(self.house)

class Father(Grandfather):
    car = "Lamborghini"

    def __init__(self) -> None:
        print("new house")
        print("self.car")
        super().__init__()

class Mother:
    jewellery = "Diamond"

class Son(Father, Mother):
    console = "PS5"

    def __init__(self) -> None:
        self
        super().__init__()


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

