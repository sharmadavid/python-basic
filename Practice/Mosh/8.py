names=['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0]='Jon'
print(names[2:])
print(names)

numbers = [1,3,-4,7,10]
max=numbers[0]
for number in numbers:
       if number>max:
        max=number
print(f"the maximum number from the list is {max}")

# 2d list
# [
#     1 2 3
#     4 5 6 
#     7 8 9 
# ]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1]=20
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)