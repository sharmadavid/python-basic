# function
# args....arguments

def sum(*numbers):
    total = 0
    for number in numbers:
        total+=number
        

    print(total)

sum(1,2,3,234,546,2345)

# kwargs
def person(**kwargs):
    print(kwargs['name'],kwargs['age'],kwargs['gender'])
          

person(name='ram', age="22", gender="male",dob="2000/1/5")

def sum(a,b):
    return a+b

sum_of=sum(1,2)
print(sum_of)

def number(n):
    print(n)
    if n == 10:
        return
    number(n+1)

number(1)

# scope
a=10

def number():
    a=11
    print(a)
    # a=11

number()
print(a)

print("global")
a=10
def number():
    global a
    a=11
    print(a)

number()
print(a)

x=9
def outer():
    x=10
    def inner():
        x=11
        print(f"inner sees x as {x}")

    inner()
    print(f"outer sees x as {x}")

outer()
print(f"global sees x as {x}")
