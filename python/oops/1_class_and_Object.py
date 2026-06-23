# ------------------------------------------
# 1. Simple Class & Object
# ------------------------------------------
class Student:
    pass

s1=Student()
print(type(s1))  # <class '__main__.Student'>

# ------------------------------------------
# 2. Instance Variables using Constructor
# ------------------------------------------

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
s1=Student("shubham" ,24)
print(s1.name)  # shubham
print(s1.age)   # 24
        

# ------------------------------------------
# 3. Instance Method
# ------------------------------------------

class student:
    def __init__(self,name):
        self.name=name
    def show(self):
        return self.name
    
s=student("Shubham")
print(s.show())  # Shubham
# ------------------------------------------
# 4. Class Variable
# ------------------------------------------

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Shubham")
s2 = Student("Rahul")

print(Student.school)
print(s1.school)
print(s2.school)

# ------------------------------------------
# 5. Class Method
# ------------------------------------------

class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()

# ------------------------------------------
# 6. Static Method
# ------------------------------------------

class Math:

    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(10, 20))
