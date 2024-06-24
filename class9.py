# print("\ndavid\n"*10)

# object oriented Programming

# object...blueprint...structure

class House:
    # attributes
    door = 10
    window = 5
    color = "red"

    def set_color(self,color):
        self.color=color

    def get_color(self):
        return self.color



ram_ko_ghar=House()
shyam_ko_ghar=House()

# print(ram_ko_ghar.color)
# print(shyam_ko_ghar.window)
# # print(ram_ko_ghar.window)

print(ram_ko_ghar.get_color())

ram_ko_ghar.set_color("green")

print(ram_ko_ghar.get_color())

print("\n"*2)

class Burger:

    def patty(self):
        print("patty")
        return self
    
    def sauce(self):
        print("sauce")
        return self
    
    def saagg(self):
        print("saagg")
        return self
    
    def bun(self):
        print("bun")
        return self
    
burger=Burger()

# burger.bun().patty().saagg().patty().sauce().bun()

burger.bun() \
    .patty() \
    .saagg() \
    .patty() \
    .sauce() \
    .bun()

print("\n"*2)

class Pizza():
    
    def base(self):
        print("base")
        return self
    
    def sauce(self):
        print("sauce")
        return self
    
    def cheese(self):
        print("cheese")
        return self
    
    def vegetables(self):
        print("vegetables")
        return self
    
    def spices(self):
        print("spices")
        return self
    

pizza=Pizza()
pizza.base().sauce().cheese().vegetables().cheese().spices()

