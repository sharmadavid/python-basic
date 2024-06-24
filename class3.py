# set datatype
A={
    1,
    345,
    2345,
    32456,
    24,
    5,
    1
}
print(A)

# dictionary datatype
person={
    'name':"Ram",
    'age':20,
    'gender':"male",
    "address":"Kathmandu",  
    "hobbies":[
        "singing",
        "dancing"
    ],
    "fav_movies":[
        "3 Idiots",
        "PK",
        "Dhoom"
                  ],
    "friends":[
        {
            "name":"Shyam"
        },
        {
            'name':"Hari"
        }
            ]
    }
# print(person)
# print(person["age"])
print(person["name"])
# print(person["fav_movies"][2])
print(person["friends"][0]['name'])
print(person["friends"][1]['name'])
# print(person["friends"][1]['fav_movies'][0])
# download code from viber


# type casting
# string, number, string, int, list, tuple, 
pie=3.14
print(type(pie))

pie=int(pie)
print(type(pie))

# a="3.14a"
# a=float(a)
# print(type(a))
# print(a)

x=float('3.14')
print(x)

x=str(42)
print(x)

# boolean datatype
isLogin=True
print(type(isLogin))
print(bool(0))
print(bool(1))
print(bool(245356))
