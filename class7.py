# # decorator

def star(func):
    def wrapper ():
        print("*"*10)
        func()
        print("*"*10)
    return wrapper


@star
def hello():
    print("Hello")

hello()

# @star
# def world():
#     print("world")

# hello()
# world()

# lambda
# def sum(a,b):
#     return a+b

# sum=lambda a,b:a+b

# print(sum(1,2))

def myfunc(n):
    return lambda a:a*n

# lambda a:a*2
doubler=myfunc(2)
triper=myfunc(3)


# anonymous function


print(doubler(3))
print(triper(3))
