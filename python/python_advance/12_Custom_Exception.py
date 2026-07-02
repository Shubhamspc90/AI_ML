
"""This example demonstrates a Custom Exception in Python."""
# class InvalidAgeError(Exception):
#     pass

# age = int(input("Enter age: "))

# if age < 18:
#     raise InvalidAgeError("Not Eligible")

# print("Eligible")

"""Better Version Using try-except
"""
class InvalidAgeError(Exception):
    pass
try:
    age=int(input("Enter Age:  "))
    if age<18:
        raise InvalidAgeError("Not eligible")
    
except InvalidAgeError as e:
    print("Error: ",e)   

except ValueError as e:
    print("Error:",e) 
    
    
##############################################################
