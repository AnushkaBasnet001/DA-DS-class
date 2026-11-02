# Login Register with ATM task


# credentials = []
credentials = [{'username': 'Ujjwal', 'password': 'Ujjwal123', 'balance': 0}, {'username': 'Ram', 'password': 'Ram123', 'balance': 0}]

def atm_option(method, username):
    for cred in credentials:
        if cred.get("username")==username:
            curr_balance = cred.get("balance")
            if method == "view":
                print(f"Your current balance is {curr_balance}")
            else:
                amount = float(input("Enter your amount: "))
                if method == "add":
                    new_balance = curr_balance + amount
                    cred.update({"balance":new_balance})
                    print(f"{amount} added Successfully")
                else:
                    new_balance = curr_balance - amount
                    cred.update({"balance":new_balance})
                    print(f"{amount} withdrawn Successfully")

                    
                
    # if method == "view":
    #     print(f"Your current balance is {curr_balance}")
    # if method == "add":
    #     new_balance = curr_balance + amount
    #     for cred in credentials:
    #         if cred.get("username") == username:
    #             cred.update({"balance":new_balance})
        
    # else:
    #     # curr - subtract amount

def operation(method):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if method == 'register':
        # register code
        # dict_cred = {username:password, "balance":0}
        dict_cred = {"username":username, "password":password, "balance":0}
        credentials.append(dict_cred)
        print("Registration successfull")
        print(credentials)
    else:
        is_login = False
        for cred in credentials:
            if cred.get("username") == username and cred.get("password") == password:
                print("Login Successfull")
                is_login = True
                use_atm = input("Do you want to use ATM? (y/n): ")
                if use_atm.lower() == "y":
                    while True:
                        # ATM MENU
                        atm_choice = input("Enter 1 to add balance, 2 to withdraw balance, 3 to view balance, 4 to exit: ")
                        match atm_choice:
                            case '1':
                                # add
                                atm_option("add", username)
                            case '2':
                                # withdraw
                                atm_option("withdraw", username)

                            case '3':
                                # view
                                atm_option("view", username)
                                    
                            case '4':
                                print("Thank your for using our ATM")
                                break
                            case _:
                                print("Invalid Input")
                        
                else:
                    return
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