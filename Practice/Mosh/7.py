
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)
    

print("nested loop method:")

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

l=[1, 1, 1, 1, 1, 5]
for count in l:
    a=''
    for b in range(count):
        a+='x '
    print(a)