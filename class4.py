# operators
a=10
b=10
c=a+b
d=a-b
e=a*b
f=a/b
g=a%b
h=a**b
i=a//b
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)

# assignment operators
x=5
x+=3
print(x)
# =
# +=
# -=
# *=
# /=
# %=
# //=
# **=

# comparison operators, returns in boolean value
# ==
# !=
# >
# <
# >=
# <=
x=10
y='11'
print(x<=int(y))

a=5
b=7
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

print('Logical Operators')
# and
# or
# not
x=7
print(x>5 and x<10)
print(x>5 or x<10)
print(x>5 and not x<10)
print(True)
print(not(False))

print("Conditional Statements")
# if
# elif
# else
# a=11
a=int(input("Enter any number:> "))

if a == 10:
    print("the value of a is", a)
elif a == 11:
    print("the value of a is", a)
else:
    print("the value of a is not 10 and 11")

print("the end")

print("ODD OR EVEN CHECK")
a=int(input("Enter a number:> "))
b=a%2
if b == 0:
    print('the number you have entered is even')
else:
    print('the number you have entered is odd')

# input number and operator