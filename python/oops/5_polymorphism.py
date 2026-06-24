# Polymorphism
"""
Polymorphism means "many forms".
In OOP, polymorphism allows the same method or function name to behave differently for different objects.
"""
class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

dog = Dog()
cat = Cat()
dog.sound()  # Dog barks
cat.sound()  # Cat meows

# Types of Polymorphism
# 1. Compile-Time Polymorphism (Method Overloading)
class Calculator:

    def add(self, a, b, c=0):
        return a + b + c

obj = Calculator()

print(obj.add(10, 20))  # 30
print(obj.add(10, 20, 30))  # 60

# 2. Run-Time Polymorphism (Method Overriding)
# When a child class provides its own implementation of a method already defined in the parent class.

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


obj = Dog()
obj.sound()  # Dog barks

""" 
Polymorphism
│
├── Compile-Time Polymorphism
│   └── Method Overloading (using default arguments)
│
└── Run-Time Polymorphism
    └── Method Overriding
"""


# Most Important Example for Interviews
class Animal:
    def sound(self):
        print("Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]
for a in animals:
    a.sound()
# output:
# Bark
# Meow