try:
    a=int(input("Enter 1st Number  "))
    b=int(input("Enter 2nd Number  "))
    print(f"{a}/{b} = {a/b}")
    
except ZeroDivisionError:
    print("ZeroDivisionError!   Can not divide with zero")
