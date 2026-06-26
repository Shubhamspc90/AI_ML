balance = 5000

amount = int(input("Enter withdrawal amount: "))

if amount > balance:
    raise ValueError("Insufficient Balance")

balance -= amount

print("Withdrawal Successful")
print("Remaining Balance:", balance)