# datatype method
from tkinter import Variable


name=" my name is DAVID sharma"
print(len(name))
print(name.lower())
print(name.upper())
print(name.strip())
print(name.split())

my_list=[1,2,3]
arko_list=[4,5,6]

print(my_list)
my_list.append((10,20))
print(my_list)
my_list.extend(arko_list)
print(my_list)

print(len(my_list))
my_list.insert(8,100)
print(my_list)
my_list.remove(100)
print(my_list)
my_list.pop(0)
print(my_list)
print(my_list.index(6))
print(my_list.sort)
print(my_list.reverse)


# list=[]

# for i in range(3):
#     print(list)
#     name = input("name:>   ")

# # dictionary
# len(dict)
# dict.keys()
# dict.values()
# dict.items()
# dict.get

people={
    'name':'ram',
    'age':30
}
print(people)
# print(people.get('name','!!'))

people.update(
    {'name':'hary',
     'age':25,
     }
)
print(people)

# # set
# len(set)
# set.add(element)
# set.remove(element)
# set.union(other_set)
# set.intersection(other_set)
# set.difference(other_set)

# user input: name, email and password......store in database (list of dictionary)......
# function
# dictionary
# global variable

