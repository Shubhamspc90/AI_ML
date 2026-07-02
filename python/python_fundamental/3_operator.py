#  # Operators in Python

#  Arithmetic Operators
print("Arithmetic Operators")
a = 10
b = 3

print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333333333333335
print(a % b)  # 1
print(a ** b) # 1000
print(a // b) # 3

# Comparision Operators
print("Comparision Operators")
a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True

# Logical Operators
print("Logical Operators")
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# Assignment Operators
print("Assignment Operators")
x = 10

x += 5
print(x)  # 15

x -= 2
print(x)  # 13

x *= 2
print(x)  # 26

# Bitwise Operators
print("Bitwise Operators")
a = 5   # 101
b = 3   # 011

print(a & b)  # 1
print(a | b)  # 7
print(a ^ b)  # 6

# Membership Operators
name = "Python"

print("P" in name)  # True
print("z" in name)  # Flase
print("z" not in name) # True

# Identity Operators
print("Identity Operators")
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True
print(a is c)  # False

print(a is not c)  # True

# Difference Between == and is
print("Difference Between == and is")
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False