"""The finally block always executes whether an exception occurs or not."""

try:
    a=int(input("Enter 1st number  "))
    b=int(input("Enter 2nd Number  "))
    print(f"{a}/{b} = {a/b}")
    
except Exception as e:
    print("error: ",e)
finally:
    print("finally block executed")