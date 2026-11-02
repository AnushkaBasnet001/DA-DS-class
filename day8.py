# Login Register Program
# Register flow:
# Ask username and password from user
# Convert them into dictionary
# Append the dictionary in the list

# Login FLow:
# Ask usernane and password from user
# Loop in the list of dictationary
# Check if username == username and dict.get(username) == password

# Note:
# Use while loop so that whenever user wants to exit
# [{'Ujjwal': 'Ujjwal123'}, {'Ram': 'Ram123'}, {'Shyam': 'Shyam123'}, {'Hari': 'Hari123'}]
user_credentials = [{'Ujjwal': 'Ujjwal123'}, {'Ram': 'Ram123'}, {'Shyam': 'Shyam123'}, {'Hari': 'Hari123'}]

while True:
    choice = input("Enter 1 for register, 2 for login, 3 for exit: ")
    match choice:
        case '1':
            # code to register
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            dict_cred = {username:password}
            user_credentials.append(dict_cred)
            print(user_credentials)
        case '2':
            # code to login
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            for cred in user_credentials:
                if username in cred and cred.get(username)==password:
                    print("Login Successfull")
                    break
            else:
                print("Login Failed")
            
        case '3':
            print("Thank you")
            break
        case _:
            print("Invalid Login")


# FOR ELSE
# If break encounters in for block, it exits from both for and else
# else, only ELSE block is executed

# dict1 = {'Ujjwal': 'Ujjwal123'}
# dict2 = {'Ram': 'Ram123'}
# username = "Ram"
# print(username in dict1)
# print(dict1.get(username))
# print(username in dict2)
# print(dict2.get(username))

# and



# Task: 
# Input: "Ujjwal Neupane"
# Result: {"U":2,
#  "j":2,
#  "w":1,
#  "a":2,
#  "l":1,
#  "N":2,
#  "e":2,
#  "p":1,
#  " ":1
#  }