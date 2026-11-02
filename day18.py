# MRO
# Method Resolution Order
# MRO gives the order of the classes to which Python visits next

# class GrandParent:
#     name = "Grand Parent"
#     def display(self):
#         print("Displaying from Grand Parent class")

# class Parent(GrandParent):
#     name = "Parent"
#     def display(self):
#         print("Displaying from Parent class")

# class Child(Parent):
#     name = "Child"
#     def display(self):
#         print("Displaying from Child class")

# c1 = Child()
# print(c1.name)
# c1.display()
# # MRO is done always of Class
# print(Child.mro())

# super() => super() is used to call the parent class's method from inside the class

# class Parent:
#     def display(self, name, age):
#         print(f"Name = {name}")
#         print(f"Age = {age}")
        
# class Child(Parent):
#     def abc(self, name, age):
#         super().display(name, age)
        

# c1 = Child()
# c1.abc("Ujjwal",27)


# class A:
#     def show(self):
#         print("A")
        
# class B(A):
#     def show(self):
#         super().show()
#         print("B")
        
# class C(A):
#     def show(self):
#         super().show()
#         print("C")
        
# class D(B,C):
#     def show(self):
#         super().show()
#         print("D")
        
# d = D()
# d.show()
# print(D.mro())


# Encapsulation
# The main idea of encapsulation is data hiding
# The hidden data cannot be accessed from outside the class, even object cannot access it
# The hidden data is only accessed from inside the class
# to hide the data, we use __ as prefix

# class Credentials:
#     username = "Ujjwal"
#     __password = "Ujjwal123"
#     abc2 = __password
    
#     def __reset_password(self,new_password):
#         print(f"Old Password = {self.__password}")
#         self.__password = new_password
#         print(f"New Password = {self.__password}")
        
#     def abc(self, new_password):
#         self.__reset_password(new_password)
    
# c1 = Credentials()
# print(c1.username)
# print(c1.abc2)
# c1.abc("Ujjwal@123#")
# print(c1.__password)



# Polymorophism
# Same form different behaviour according to the class
# print(5+10)
# print('5'+'10')

class Dog:
    name = "Dog"
    def eat(self):
        print("Dog is eating bones")
        
class Cat:
    name = "Cat"
    def eat(self):
        print("Cat is eating milk")
        
class Human:
    name = "Human"
    def eat(self):
        print("Human is eating rice")
        
d1 = Dog()
c1 = Cat()
h1 = Human()
print(d1.name)
d1.eat()
print()
print(c1.name)
c1.eat()
print()
print(h1.name)
h1.eat()
print()