# loops
# primitive loop: while and for

# while True:

i=0
while i<=10:
    print(i)
    if i == 5:
        break
    i+=1

# range datatype

numbers=range(1,20,2)
print(list(numbers))

a=[1,2,3,4,5]
# print(2 in a)
for i in range(1,11):
    print(i)

fruits=(
    "apple",
    "kiwi",
    "chocolate",
    "orange",
    "grapes"
)

for a in fruits:
    print("my favourite fruit is " + a)
    print(f"my favourite fruit is {a}")
    if a == "orange":
        break

# using for loop print each character

# multiplication table of user input number

# function
    
def greet(name,age):
    print(f"Hello {name}({age})!")
    print(f"{name}!! How are you!! 😊")

greet("Ram",20)

def person(name,age,gender):
    print(f"""
        Hello!! my name is {name} and my age is {age}
        and my gender is {gender}
          """)
    
person("Micheal",25,"Male")