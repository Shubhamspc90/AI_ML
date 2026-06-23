# FUNCTIONS IN PYTHON

# ------------------------------------------
# 1. Function Without Parameters & Without Return
# ------------------------------------------

def greet():
    print("Hello World")

greet()  # Hello World

# ------------------------------------------
# 2. Function With Parameters & Without Return
# ------------------------------------------

def greet(name):
    print("Hello", name)

greet("Shubham")  # Hello Shubham

# ------------------------------------------
# 3. Function Without Parameters But With Return
# ------------------------------------------

def get_num():
    return 100

x = get_num()
print(x)  # 100

# ------------------------------------------
# 4. Function With Parameters & Return
# ------------------------------------------

def add(a, b):
    return a + b

print(add(10, 20))  # 30

# ------------------------------------------
# 5. Positional Arguments
# ------------------------------------------

def student(name, age):
    print(name, age)

student("Shubham", 24)  # Shubham 24

# ------------------------------------------
# 6. Keyword Arguments
# ------------------------------------------

student(age=24, name="Shubham")  # Shubham 24

# ------------------------------------------
# 7. Default Arguments
# ------------------------------------------

def greet(name="Guest"):
    print("Hello", name)

greet()  # Hello Guest
greet("Shubham")  # Hello Shubham

# ------------------------------------------
# 8. Variable Length Arguments (*args)
# ------------------------------------------

def total(*args):
    print(sum(args))

total(10, 20, 30, 40)  # 100

# ------------------------------------------
# 9. Keyword Variable Length Arguments (**kwargs)
# ------------------------------------------

def info(**kwargs):
    print(kwargs)

info(name="Shubham", age=24)  # {'name': 'Shubham', 'age': 24}

# ------------------------------------------
# 10. Return Statement
# ------------------------------------------

def square(n):
    return n * n

print(square(5))  # 25

# ------------------------------------------
# 11. Lambda Function
# ------------------------------------------

square = lambda x: x * x

print(square(5))  # 25

# ------------------------------------------
# 12. Recursion
# ------------------------------------------

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))  # 120

# ------------------------------------------
# 13. Local Variable
# ------------------------------------------

def demo():
    x = 10
    print("Local Variable:", x)

demo()  #  Local Variable: 10

# ------------------------------------------
# 14. Global Variable
# ------------------------------------------

x = 100

def demo():
    print("Global Variable:", x)

demo()  # Global Variable: 100

# ------------------------------------------
# 15. Nested Function
# ------------------------------------------

def outer():

    def inner():
        print("Inner Function")

    inner()

outer()  # Inner Function

# ------------------------------------------
# 16. Function Returning Multiple Values
# ------------------------------------------

def calc(a, b):
    return a+b, a-b

sum1, sub1 = calc(10, 5)

print(sum1)  # 15
print(sub1)  # 5

# ------------------------------------------
# 17. Built-in Functions
# ------------------------------------------

nums = [10, 20, 30, 40]

print(len(nums))  # 4
print(max(nums))  # 40
print(min(nums))  # 10
print(sum(nums))  # 100
print(sorted(nums))  # [10, 20, 30, 40]
print(type(nums))  # <class 'list'>
print(id(nums))  # 3052913758592

# ------------------------------------------
# 18. Anonymous Lambda Examples
# ------------------------------------------

add = lambda a, b: a + b
print(add(10, 20))  # 30

even = lambda x: x % 2 == 0
print(even(10))  # True

# ------------------------------------------
# 19. Scope Example
# ------------------------------------------

x = 50

def test():
    x = 100
    print("Inside Function:", x)
 
test()  # Inside Function: 100
print("Outside Function:", x)  # Outside Function: 50

# ------------------------------------------
# 20. Recursive Fibonacci
# ------------------------------------------

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i), end=" ")

print()  # 0 1 1 2 3 5 8 13 21 34 

# ------------------------------------------
# MOST IMPORTANT FUNCTION CONCEPTS
# ------------------------------------------

# Function Definition      -> def
# Function Call            -> func()
# Parameters
# Arguments
# Return Statement
# Positional Arguments
# Keyword Arguments
# Default Arguments
# *args
# **kwargs
# Lambda Function
# Recursion
# Local Variable
# Global Variable
# Nested Function
# Multiple Return Values

# ------------------------------------------
# MOST IMPORTANT INTERVIEW QUESTIONS
# ------------------------------------------

# Factorial using Function
# Prime Number using Function
# Fibonacci using Recursion
# Palindrome using Function
# Reverse String using Function
# Count Vowels using Function
# Sum using *args
# Student Details using **kwargs
# Largest Element using Function
# Character Frequency using Function