a = int(input("enter first number:> "))
b = int(input("enter second number:> "))
op = input("enter the operator:> ")

if op == '+':
    print("the result is:> ", a+b)
elif op == '-':
    print("the result is:> ", a-b)
elif op == '*':
    print("the result is:> ", a*b)
elif op == '/':
    if b == 0:
        print("cannot divide by 0, Mathematical Error")
    else:    
        print("the result is:> ", a/b)
elif op == '%':
    print("the result is:> ", a%b)
elif op == '**':
    print("the result is:> ", a**b)
elif op == '//':
    print("the result is:> ", a//b)
else:
    print("the operator is not recognized")
