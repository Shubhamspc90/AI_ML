
# Exception Handling in Python
"""Exception Handling is used to handle runtime errors and prevent the program from crashing."""

try:
    num = int(input("Enter number: "))
    print(100 / num)

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("No error occurred")

finally:
    print("Program ended")
    
    

"""Common Python Exceptions (Notes)
"""
# ZeroDivisionError
# Occurs when a number is divided by zero.

# ValueError
# Occurs when a function receives a valid data type but an invalid value.

# TypeError
# Occurs when an operation is performed on incompatible data types.

# IndexError
# Occurs when accessing an index that is out of range.

# KeyError
# Occurs when accessing a dictionary key that does not exist.

# NameError
# Occurs when a variable or name is not defined.

# FileNotFoundError
# Occurs when trying to open a file that does not exist.

# AttributeError
# Occurs when an object does not have the requested attribute or method.

# ImportError
# Occurs when Python cannot import a module or object.

# ModuleNotFoundError
# Occurs when the specified module cannot be found.

# OverflowError
# Occurs when a calculation exceeds the maximum limit allowed by Python.

# RecursionError
# Occurs when the maximum recursion depth is exceeded.

# SyntaxError
# Occurs when Python encounters invalid syntax.

# IndentationError
# Occurs when code indentation is incorrect.

# PermissionError
# Occurs when the program lacks permission to access a file or resource.

# MemoryError
# Occurs when the system runs out of memory.

# KeyboardInterrupt
# Occurs when the user manually interrupts the program (e.g., Ctrl + C).

"""Exception Handling Keywords
"""
# try
# Contains code that may raise an exception.

# except
# Handles the exception if it occurs.

# else
# Executes if no exception occurs.

# finally
# Always executes, whether an exception occurs or not.

# raise
# Used to manually trigger an exception.
