number=int(input("Enter a number:> "))
count = 1
print("Multiplication Table")
while count <= 10:
    print(f"{number} x {count} = {number*count}")
    count +=1

number=int(input("Enter a number:> "))
count = 1
print("""
      
      
Multiplication Table""")
for i in range (1,11):
    print(f"{number} x {i} = {number*i}")
