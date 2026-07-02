""" 
Abstraction
Imagine a car:
You use the steering, brake, and accelerator.
You do not need to know how the engine, gearbox, or fuel injection system works internally.

This is Abstraction:
Showing only essential features and hiding implementation details.
"""

from abc import ABC, abstractmethod
class Animal(ABC):  # Abstract Class

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

dog = Dog()
dog.sound()  # Dog barks



# Real-Life Example
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("Paid using UPI")

class CreditCard(Payment):
    def pay(self):
        print("Paid using Credit Card")


p = UPI()
p.pay()  # Paid using UPI