# Inheritance
print("\nInheritance")
class Parent:

    def show(self):
        print("Parent Class")

class Child(Parent):
    pass

c1 = Child()
c1.show()  # Parent Class


# Single Inheritance
print("\nSingle Inheritance")
class Animal:

    def eat(self):
        print("Eating")

class Dog(Animal):

    def bark(self):
        print("Barking")

d = Dog()

d.eat()  # Eating
d.bark()  # Barking


# Multilevel Inheritance
print("\n Multilevel Inheritance")
class A:

    def showA(self):
        print("Class A")

class B(A):

    def showB(self):
        print("Class B")

class C(B):

    def showC(self):
        print("Class C")

obj = C()

obj.showA()  # Class A
obj.showB()  # Class B
obj.showC()  # Class C


#  Multiple Inheritance
print("\nMultiple Inheritance")
class Father:

    def father_property(self):
        print("Father Property")

class Mother:

    def mother_property(self):
        print("Mother Property")

class Child(Father, Mother):
    pass

c = Child()

c.father_property()  # Father Property
c.mother_property()  # Mother Property


# Hierarchical Inheritance
print("\n Hierarchical Inheritance")
class Parent:

    def show(self):
        print("Parent")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()

c1.show()  # Parent
c2.show()  # Parent


# Method Overriding
print("\nMethod Overriding")
class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Dog Barks")

d = Dog()
d.sound()  # Dog Barks


# super() Method
print("\nsuper() Method")
class Parent:

    def __init__(self):
        print("Parent Constructor")

class Child(Parent):

    def __init__(self):
        super().__init__()
        print("Child Constructor")

c = Child()
# output
# Parent Constructor
# Child Constructor