# access modifier

class Person():
    
    def __init__(self, name, salary, password) -> None:
        self.name = name # public
        self._salary = salary #protected
        self.__password = password #private, only in its class and subclass

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

ram = Person("ram", 12, "123")
ram.set_password("1234")
print(ram.get_password())

# with decorator
print("\nEasier Method")

class Person():
    
    def __init__(self, name, salary, password) -> None:
        self.name = name # public
        self._salary = salary #protected
        self.__password = password #private, only in its class and subclass

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

ram = Person("ram", 12, "123")
ram.password="1234"
print(ram.password)

# abstaction
print("\nAbstraction\n")

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self, app):
        pass

    def run(self, app):
        self.process(app)

class Laptop(Computer):
    def process(self, app):
        print(f"Laptop is running {app}")

dell = Laptop()
dell.run("PUBG")

# black formatter
#  copy django
# flake 8
#  ignore
# indentrainbow
#  intelligence code
# isort
# pylance, python
# tab9

