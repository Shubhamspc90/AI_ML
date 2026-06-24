# Encapsulation
""" 
Encapsulation in Python

Encapsulation is an OOP concept that means binding data (variables) and methods (functions) together in a single unit (class) and restricting direct access to some data.

In simple words:

Encapsulation = Data Hiding + Controlled Access

Real-Life Example

Think of an ATM Machine.

You can withdraw money using the buttons provided.
You cannot directly access or modify the bank's database.

The ATM hides the internal details and provides controlled access.
"""

# Define a class named Employee
class Employee:

    # Constructor: called automatically when an object is created
    def __init__(self, salary):
        # Private attribute (__salary)
        # Double underscore (__) makes it private
        self.__salary = salary

    # Getter method to access the private salary attribute
    def get_salary(self):
        return self.__salary


# Create an object of Employee class and pass salary
e1 = Employee(50000)

# Call the getter method to retrieve salary
print(e1.get_salary())  # Output: 50000
# print(e1.__salary)  # AttributeError: 'Employee' object has no attribute '__salary'


#Here's another simple Encapsulation (Private Variable) example using a Bank Account.
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance   # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


# Create object
acc1 = BankAccount(1000)

# Deposit money
acc1.deposit(500)

# Access balance using method
print("Balance:", acc1.get_balance())

# print(acc1.__balance)  # Direct access (will cause error)