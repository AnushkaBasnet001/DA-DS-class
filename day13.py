# Login Register using File

# Register FLow:
# Ask username password from user
# Write the dictionary of username:password in file
# We can only write string or json in file

# Login FLow:
# Ask username password from user
# Read all the creds in the file
# We can read the creds in the form of string or json
# CHeck for each cred if username and password matches or not
# login successfull if matched else login failed

import json
# json.dumps() => Converts dictionary to json
# json.loads() => Converts json to dictionary

def atm_task(method, username):
    file = open("Credentials2.txt","r")
    content = file.read()
    file.close()
    list_creds = content.split("*")
    credentials = ""
    for i in list_creds:
        if i != "":
            dict_i = json.loads(i)
            if dict_i.get("username")==username:
                curr_balance = dict_i.get("balance")
                if method == 'view':
                    print(f"Your current balance is {curr_balance}")
                    return
                else:
                    amount = float(input("Enter the amount: "))
                    if method == "add":
                        new_balance = curr_balance+amount
                        dict_i.update({"balance":new_balance})
                    else:
                        new_balance = curr_balance-amount
                        dict_i.update({"balance":new_balance})
                    credentials+=json.dumps(dict_i)+"*"
            else:
                credentials+=json.dumps(dict_i)+"*"
    file = open("Credentials2.txt","w")
    file.write(credentials)
    file.close()
    
                
            
    

def operation(method):
    username = input("Enter your username: ")
    password = input("ENter your password: ")
    if method == "register":
        # register 
        # dict_cred = {username:password}
        dict_cred = {"username":username, "password":password, "balance":0}
        file = open("Credentials2.txt","a")
        json_cred = json.dumps(dict_cred)
        file.write(json_cred+"*")
        file.close()
    else:
        # login
        file = open("Credentials2.txt","r")
        content = file.read()
        file.close()
        list_creds = content.split("*")
        is_login = False
        for i in list_creds:
            if i != "":
                dict_i = json.loads(i)
                if dict_i.get("username")==username and dict_i.get("password")==password:
                    print("Login Successful")
                    is_login=True
                    while True:
                        choice = input("Enter 1 to add balance, 2 to withdraw balance, 3 to view balance, 4 to exit: ")
                        match choice:
                            case '1':
                                # add
                                atm_task("add", username)
                            case '2':
                                # withdraw
                                atm_task("withdraw", username)
                            case '3':
                                # view
                                atm_task("view", username)
                            case '4':
                                print("Thank you for using our ATM")
                                break
                            case _:
                                print("Invalid Input")
                        
        if not is_login:
            print("Login Failed")
                
                

while True:
    choice = input("Enter 1 for register, 2 for login, 3 for exit: ")
    match choice:
        case '1':
            operation('register')
        case '2':
            operation('login')
        case '3':
            print("Thank you")
            break
        case _:
            print("Invalid Input")