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