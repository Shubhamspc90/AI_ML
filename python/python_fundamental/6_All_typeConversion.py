"""In Python, type conversion means converting one data type into another."""
# list()      # Convert to List
# tuple()     # Convert to Tuple
# set()       # Convert to Set
# dict()      # Convert to Dictionary
# str()       # Convert to String
# int()       # Convert to Integer
# float()     # Convert to Float
# bool()      # Convert to Boolean


# List → Tuple
print("\nList → Tuple")
my_list=[1,2,3,4,5]
my_tuple=tuple(my_list)
print(my_tuple)
print(type(my_tuple))

# Tuple → List
print("\nTuple → List")
my_tpl=(1,2,3,4,5)
my_lst=list(my_tpl)
print(my_lst)
print(type(my_lst))

# List -> Set
print("\nList -> Set")
l1=[1,2,3,4,5]
s1=set(l1)
print(s1)
print(type(s1))

# Set -> List
print("\nSet -> List")
my_set ={1,2,3,4,5}
l2=list(my_set)
print(l2)
print(type(l2))

# String → List
print("\nString → List")
text = "Shubham"
l3=list(text)
print(l3)
print(type(l3))

# List -> String
print("\nList -> String")
l4=["I" , "Love" ,"Python"]
my_str=" ".join(l4)
print(my_str)
print(type(my_str))

# String → Tuple
print("\nString → Tuple")
text = "Python"
result = tuple(text)
print(result)

# Tuple → Set
print("\nTuple → Set")
t = (1, 2, 3, 2)
s = set(t)
print(s)
print(type(s))

# Set → Tuple
print("\nSet → Tuple")
s = {1, 2, 3}
t = tuple(s)
print(t)
print(type(t))

# String → Integer
print("\nString → Integer")
num = "100"
x = int(num)
print(x)
print(type(x))

# Integer → String
num = 100
s = str(num)
print(s)
print(type(s))

# Integer → Float
print("\nInteger → Float")
x = 10
y = float(x)
print(y)
print(type(y))

# Float → Integer
x = 10.99
y = int(x)
print(y)
print(type(y))

