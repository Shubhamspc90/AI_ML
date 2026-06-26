try:
    a=int(input("Enter 1st Number  "))
    b=int(input("Enter 2nd Number  "))
    print(f"{a}/{b} = {a/b}")

except ZeroDivisionError:
    print("Can not divide by zero")
except ValueError:
    print("Please Enter valid input")
except Exception as e:
    print("Error: ",e)
else:
    print("else block executed")
finally:
    print("finally block executed")