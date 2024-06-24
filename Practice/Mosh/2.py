is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

# is_goodcredit = True

# if is_goodcredit:
#     print("you need to put down 10%")
#     pd=0.1 * 1000000
#     print(int(pd))
# else:
#     print("you need to put down 20%")
#     pd=0.2 * 1000000
#     print(int(pd))

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")

has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loans")

# and both condition
# or at least one
# not inverse boolean value
    

temp = 35
if temp <= 30:
    print("it's a hot day")
else:
    print("it's not a hot day")

#   <
#   <=
#   >
#   >=
#   ==
#   !=

name="David"
l=len(name)
if l<3:
    print('name must be at least 3 characters!')
elif l>50:
    print('name can be a maximum of 50 characters!')
else:
    print('name looks good!')
