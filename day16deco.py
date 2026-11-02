#day16

#decorators
# decorators are special kind of function, that receives another function as an argument
#decorator has a nested function
#decorator is used to modify the received function without changing its orginal code
#we should use decorator by adding decorator name just above the function and using @ as prefix


def my_decorator(func):
    def wrapper():
        for i in range(5):
            func()
    return wrapper

@my_decorator
def display():
    print("HI I am anushka")

display()

#we only use pre-built decorator in python
#we don't need to create our own decorator
#staticmethod
#abstract method

#staticmethod

class Students:
    def __init__(self, name, age, marks):
        self.name=name
        self.age=age
        self.marks=marks
    
    def display(self):
        print("Name: ", self.name)
        print("age: ", self.age)
        print("marks: ", marks)
        print()

    @staticmethod
    def abc():
        print("ABC")

std1=Students
std1.abc()