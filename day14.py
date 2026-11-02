# Exception Handling
# Error Handling

# try :
# In try block we write the code that may raise an error
# if error occured then expect block is executed
# else try block gets executed

# expect
# In expect we write the code that is executed if wrror occured in try block

# GENERAL ERROR HANDLING
# list1 = [1,2,3,4,5]
# try:
#     print(list1[2])
#     num1 = int(input("ENter number 1: "))
#     num2 = int(input("Enter number 2: "))
#     print(num1/num2)
# except:
#     print("An error occured")



# SPECIFIC ERROR HANDLING
# list1 = [1,2,3,4,5]
# try:
#     print(list1[2])
#     num1 = int(input("ENter number 1: "))
#     num2 = int(input("Enter number 2: "))
#     print(num1/num2)
#     file = open("aaa.txt","r")
#     file.close()
# except IndexError:
#     print("Index not found")
# except ValueError:
#     print("Cannot conert into integer")
# except ZeroDivisionError:
#     print("Num 2 cannot be 0")
# except FileNotFoundError:
#     file = open("aaa.txt","w")
#     file.close()

# Specific error handling with initial error message
list1 = [1,2,3,4,5]
try:
    print(list1[2])
    num1 = int(input("ENter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(num1/num2)
    file = open("aaa.txt","r")
    file.close()
except IndexError as ie:
    print(ie)
except ValueError as ve:
    print(ve)
except ZeroDivisionError as ze:
    print(ze)




# RECOMMENDED WAY
# list1 = [1,2,3,4,5]
# try:
#     print(list1[2])
#     num1 = int(input("ENter number 1: "))
#     num2 = int(input("Enter number 2: "))
#     print(num1/num2)
#     try:
#         abc = 10
#     except:
#         print("Okay")
# except Exception as e:
#     print("An error occured: ", e)
#     try:
#         abc = 10
#         try:
#             abc = 10
#         except:
#             print("Okay")
#     except:
#         print("Okay")
# finally:
#     print("It is ecexuted or printed anyways")
    
    
# Finally
# FInally block is executed either when error is occured or not

# Update the programs using try except


# Nested try except


# list2 = [5,6,7,8]
# try:
#     print(list2[2])
# finally:
#     print("This is finally block")