try:
    a=int(input("Enter 1st number  "))
    b=int(input("Enter 2nd Number  "))
    print(f"{a}/{b} = {a/b}")
    
except ZeroDivisionError:
    print("ZeroDivision Error!  ,  Can not divide with zero")
    
except ValueError:
    print("Value Error!")
    
