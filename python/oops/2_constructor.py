"""In Python, a constructor is a special method that is automatically called when an object is created. 
The constructor is defined using the __init__() method."""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object
p1 = Person("Shubham", 23)

print(p1.name)  # Shubham
print(p1.age)   # 23

# Default Constructor
class Student:
    def __init__(self):
        print("Student object created")

s = Student()  # Student object created

# Parameterized Constructor
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

c = Car("Toyota", "Camry")
print(c.brand, c.model)  # Toyota Camry

# Multiple Constructors?
""" 
Python does not support constructor overloading directly.
You can achieve similar behavior using default arguments:
"""

class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

e1 = Employee("John")
e2 = Employee("John", 50000)

print(e1.salary)  # 0
print(e2.salary)  # 50000

# So, in Python, the constructor is the __init__() method used to initialize an object when it is created.

# Destructor
class Demo:

    def __del__(self):
        print("Destructor Called")

d = Demo()
del d


# 20. Instance, Class and Static Method
class Demo:

    def instance_method(self):
        print("Instance Method")

    @classmethod
    def class_method(cls):
        print("Class Method")

    @staticmethod
    def static_method():
        print("Static Method")

obj = Demo()

obj.instance_method()
Demo.class_method()
Demo.static_method()
