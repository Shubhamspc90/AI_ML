
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