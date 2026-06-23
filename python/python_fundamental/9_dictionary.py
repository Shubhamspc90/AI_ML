
# ==========================================
# MOST IMPORTANT METHODS
# ==========================================
"""
get()
keys()
values()
items()
update()
pop()
popitem()
clear()
copy()
setdefault()
fromkeys()
"""
# ==========================================
# MOST IMPORTANT OPERATIONS
# ==========================================

# Accessing           -> d[key], get()
# Add / Update        -> d[key] = value
# Delete              -> pop(), del
# Traversal           -> for key, value in d.items()
# Membership          -> in, not in
# Merge               -> |
# Conversion          -> list(), tuple(), dict()
# Comprehension       -> {k:v for ...}

# ==========================================
# DICTIONARY METHODS, OPERATIONS & CONVERSIONS
# ==========================================

# Creating Dictionary
student = {
    "name": "Shubham",
    "age": 24,
    "city": "Delhi"
}

print("Original Dictionary:")
print(student)  # {'name': 'Shubham', 'age': 24, 'city': 'Delhi'}

# ==========================================
# ACCESSING VALUES
# ==========================================

print("\nAccessing Values")

print(student["name"])  # Shubham
print(student.get("age"))  # 24

# ==========================================
# ADDING / UPDATING ELEMENTS
# ==========================================

print("\nAdding / Updating")

student["email"] = "abc@gmail.com"
print(student)  # {'name': 'Shubham', 'age': 24, 'city': 'Delhi', 'email': 'abc@gmail.com'}

student["age"] = 25
print(student)  # {'name': 'Shubham', 'age': 25, 'city': 'Delhi', 'email': 'abc@gmail.com'}

student.update({"city": "Noida"})
print(student)  # {'name': 'Shubham', 'age': 25, 'city': 'Noida', 'email': 'abc@gmail.com'}

# ==========================================
# REMOVING ELEMENTS
# ==========================================

print("\nRemoving Elements")

temp = student.copy()

temp.pop("email")
print(temp)  # {'name': 'Shubham', 'age': 25, 'city': 'Noida'}

temp.popitem()
print(temp)  # {'name': 'Shubham', 'age': 25}

del temp["age"]
print(temp)  # {'name': 'Shubham'}

temp.clear()
print(temp)  # {}

# ==========================================
# DICTIONARY METHODS
# ==========================================

student = {
    "name": "Shubham",
    "age": 24,
    "city": "Delhi"
}

print("\nDictionary Methods")

print(student.keys())  # dict_keys(['name', 'age', 'city'])
print(student.values())  # dict_values(['Shubham', 24, 'Delhi'])
print(student.items())  # dict_items([('name', 'Shubham'), ('age', 24), ('city', 'Delhi')])

# ==========================================
# COPY
# ==========================================

new_dict = student.copy()
print("\nCopy")
print(new_dict)  # {'name': 'Shubham', 'age': 24, 'city': 'Delhi'}

# ==========================================
# SETDEFAULT
# ==========================================

print("\nsetdefault()")

student.setdefault("country", "India")
print(student)  # {'name': 'Shubham', 'age': 24, 'city': 'Delhi', 'country': 'India'}
# "country" key does not exist.
# So setdefault() adds it with value "India".

student.setdefault("name", "Rahul")
print(student)  # {'name': 'Shubham', 'age': 24, 'city': 'Delhi', 'country': 'India'}
# "name" key already exists.
# setdefault() does not overwrite existing values.
# Therefore "Shubham" remains unchanged.



# ==========================================
# FROMKEYS
# ==========================================

print("\nfromkeys()")

keys = ["name", "age", "city"]

new_dict = dict.fromkeys(keys, 0)

print(new_dict)  # {'name': 0, 'age': 0, 'city': 0}

# ==========================================
# TRAVERSAL
# ==========================================

print("\nTraversal")

for key in student:
    print(key)

for value in student.values():
    print(value  )

for key, value in student.items():
    print(key , value )

# ==========================================
# MEMBERSHIP OPERATORS
# ==========================================

print("\nMembership Operators")

print("name" in student)  # True
print("salary" not in student)  # True

# ==========================================
# BUILT-IN FUNCTIONS
# ==========================================

print("\nBuilt-in Functions")

print(len(student))  # 4

print(sorted(student))  # ['age', 'city', 'country', 'name']

print(min(student))  # age

print(max(student))  # name

# ==========================================
# NESTED DICTIONARY
# ==========================================

print("\nNested Dictionary")

employees = {
    101: {"name": "Amit", "age": 25},
    102: {"name": "Ravi", "age": 30}
}

print(employees)  # {101: {'name': 'Amit', 'age': 25}, 102: {'name': 'Ravi', 'age': 30}}

print(employees[101]["name"])  # Amit

# ==========================================
# TYPE CONVERSION
# ==========================================

print("\nType Conversion")

print(list(student.keys()))  # ['name', 'age', 'city', 'country']
print(list(student.values()))  # ['Shubham', 24, 'Delhi', 'India']
print(tuple(student.items()))  # (('name', 'Shubham'), ('age', 24), ('city', 'Delhi'), ('country', 'India'))

# List of Tuples -> Dictionary
data = [("a", 1), ("b", 2), ("c", 3)]

d = dict(data)

print(d)  # {'a': 1, 'b': 2, 'c': 3}

# ==========================================
# DICTIONARY COMPREHENSION
# ==========================================

print("\nDictionary Comprehension")

square = {x: x*x for x in range(1, 6)}

print(square)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# ==========================================
# MERGING DICTIONARIES
# ==========================================

print("\nMerging Dictionaries")

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

merged = d1 | d2

print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
