numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)

numbers.insert(0, 10)
print(numbers)

numbers.remove(5)
print(numbers)

# numbers.clear()
# print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(10))
# print(numbers.index(555))

numb = [5, 2, 1, 7, 4]
print(50 in numb)

numbers = [5, 2, 1, 5, 7, 4]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers = [5, 2, 1, 5, 7, 4]
numbers2 = numbers.copy()
numbers.append(10)

print(numbers2)

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
# a=uniques.sort()
print(uniques)

a=uniques.sort()
print(a)

# # tuples-immutable
# numberss = (1,2,3)
# numberss [0] = 10
# print(numbers)

# unpacking
coordinates = [1, 2, 3]
# coordinates[0] * coordinates[1] * coordinates[2]
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
x, y, z =coordinates
print (x,y,z)

# dictionaries
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
print(customer.get("birthdate", "Jan 1 1980"))
# default value

customer["birthdate"]="22 July 1994"
print(customer["birthdate"])

# number to words
phone = input("Phone: ")
digits_mapping = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
#  gives output as ! because 1,2,3,4are only defined in dictionary
print (output)

message  = input(">")
words = message.split(' ')
emojis = {
    ":)":"😊",
    ":()":"😒",
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print (output)

()