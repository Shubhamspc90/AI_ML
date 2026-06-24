"""You can create exceptions manually using raise."""

# age=int(input("enter your age  "))
# if age<18:
#     raise ValueError("age must be 18 or greater")
# print("Eligible")
     
################################################
# Using raise with try-except
try:
    age = int(input("Enter age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above")

    print("Eligible")

except ValueError as e:
    print("Error:", e)
    
    
#######################################################
# Common Exceptions Raised Manually
# 1.ValueError
num = int(input("Enter a positive number: "))

if num <= 0:
    raise ValueError("Number must be positive")


#########################################################
# 2. TypeError
name = 123

if not isinstance(name, str):
    raise TypeError("Name must be a string")


######################################################
# 3. ZeroDivisionError
denominator = int(input("Enter denominator: "))

if denominator == 0:
    raise ZeroDivisionError("Denominator cannot be zero")

##############################################################
# 4.PermissionError
is_admin = False

if not is_admin:
    raise PermissionError("Access Denied")

