# 4 Pillars of OOP
# 1. Inheritance
# 2. Encapsulation
# 3. Abstraction
# 4. Polymorphism


# 1. Inheritance
# The child class can access the properties of the parent class
# Eg:
# class Dog:
#     ears = 2
#     legs = 4
#     eyes = 2
    
#     def sound(self):
#         print("Bark")
    
#     def eats(self):
#         print("Bones")
    
# class GermanShepard(Dog):
#     color = "Generally Black and Brown"
#     pointed_ears = True
#     height = "105cm"
#     weight = "greater than 50kg"
#     # eyes = 5
    
# class GoldenRetriever(Dog):
#     color = "Mostly Golden"
#     pointed_ears = False
#     height = "105cm"
#     weight = "greater than 50kg"

# Task: Update this example by using object attribute and using the constructor
    
    
# dog1 = Dog()
# print(dog1.ears)
# dog1.eats()

# gs1 = GermanShepard()
# print(gs1.color)
# print(gs1.pointed_ears)
# gs1.eats()
# print(gs1.eyes)
# Types:
    # 1. Single Inheritance
        # -> One Child class inherits from only one parent class
# class Parent:
#     name = "Parent"
    
#     def display(self):
#         print("DIsplaying from Parent Class")
        
# class Child(Parent):
#     name = "Child"
    
#     def display(self):
#         print("Displaying from Child class")
        
# c1 = Child()
# print(c1.name)
# c1.display()

# Property Overriding
# The child class has the same property of parent class 


    # 2. Multiple Inheritance
        # One child class inherits from multiple parent classes
# class Parent1:
#     name = "Parent1"
#     def display(self):
#         print("Displaying from Parent1 class")
        
# class Parent2:
#     name = "Parent2"
#     def display(self):
#         print("Displaying from Parent2 class")
        
# class Child(Parent2,Parent1):
#     pass
#     # name = "Child"
#     # def display(self):
#     #     print("Displaying from Child class")
        
# c1 = Child()
# print(c1.name)
# c1.display()


    # 3. Multi-level Inheritance
        # First, Child inherits from Parent class
        # Then, Parent inherits from GrandParent class
        # So, ultimately, Child class can access the properties of GrandParent class also
        
class GrandParent:
    name = "Grand Parent"
    def display(self):
        print("Displaying from Grand Parent class")
        
class Parent(GrandParent):
    pass
    # name = "Parent"
    # def display(self):
    #     print("Displaying from Parent class")
        
class Child(Parent):
    pass
    # name = "Child"
    # def display(self):
    #     print("Displaying from Child class")
        
c1 = Child()
print(c1.name)
c1.display()

# Task: Update this example by using object attribute and using the constructor
# Task: Research on MRO in inheritance