# Abstraction
# The main idea of abstraction is showing what is needed hiding the implementation details


# abstractmethod
# conditions:
# 1. The parent class should have inherited from ABC(Abstract Base Class)
# 2. The parent class should have atleast one abstractmethod
# 3. The child class should inherit from Parent class

# If these 3 conditions are satisfied, then
# Every child class that inherits from Parent class should also have abstractmethod

# from abc import ABC, abstractmethod

# class Teacher(ABC):
#     name = "Teacher"
    
#     @abstractmethod
#     def teaches(self):
#         print("I am a teacher")
        
# class EnglishTeacher(Teacher):
#     name = "English Teacher"
    
#     def teaches(self):
#         print("I am a English teacher")
        
# class MathTeacher(Teacher):
#     name = "Math Teacher"
    
#     def teaches(self):
#         print("I am a Math teacher")
        
# class ComputerTeacher(ABC):
#     name = "Computer Teacher"
    
#     # def teaches(self):
#     #     print("I am a Computer teacher")
#     #     for i in range(5):
#     #         print(i)
        
# c1 = ComputerTeacher()
# m1 = MathTeacher()
# e1 = EnglishTeacher()
# print(c1.name)
# # c1.teaches()
# print()
# print(m1.name)
# m1.teaches()
# print()
# print(e1.name)
# e1.teaches()
# print()




# Magic Methods
# Magic methods are the special type of methods that executes automatically under 
# certain condition
# Magic method starts and ends with __

# __init__ => RUns automatically when an object is created
# __str__ => Runs automatically when an object is printed
# __str__ always returns a value
# __add__ => + automatically calss __add__ 
# __sub__ => - automatically calss __sub__ 
# __mul__ => * automatically calss __mul__ 
# __new__ => Task: read on this


# class Number:
#     def __init__(self, value):
#         self.value = value
        
#     def __str__(self):
#         return f"{self.value} object is being printed"
    
#     def __add__(self, other):
#         return f"The addition is {self.value+other.value}. Ujjwal Neupane"
        
        
# n1 = Number(12)
# print(n1.value)
# print(n1)
# print()
# n2 = Number(20)
# print(n2.value)
# print(n2)

# print(n1.value+n2.value)
# print(n1+n2)


class Car:
    def model(self):
        print("The model name should be in front of the brand name. FOr eg: Hyundai i10, Hyundai i20")