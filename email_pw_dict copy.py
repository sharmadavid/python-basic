def collect_data():
    user_data={}

    while True:
        name = input ("Enter Your Name:  ")
        email = input ("Enter Yout Email:  ")
        password = input ("Enter Your Password:  ")

        user_data[name] = {
            "email":email,
            "password":password
        }

        add_another = input("Add Another User Data? (Y/N): ").upper()
        if add_another == 'N':
            break

    return user_data

# def main():
#     user_data = collect_data()
#     print(".....All Database.....")
    
#     for name, details in user_data.items():
#         print(f"Name: {name}, Email: {details['email']}, Password: {details['password']}")

def check_user_data(user_data):

    # print("Login For Accessing Database:   ")

    name_check = input ("Enter your name to verify:   ")
    # email_check = input("Enter your email to verify:  ")
    # password_check = input ("Enter your password to verify: ")
   

#yaha bigreko jasto lagcha
    # if email_check in user_data[name]['email'] == email_check and user_data[name]['password' == password_check]:
    #     print(".....All Database.....")
    if name in user_data == name_check:
        for name, details in user_data.items():
            print(f"Name: {name}, Email: {details['email']}, Password: {details['password']}")
    else:
        print(".....Creddentials Mismatch.....")

user_data = collect_data()
# user_data()

check_user_data(user_data)
# main()
