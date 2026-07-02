
# TUPLE IN PYTHON

# Creating a tuple
t = (10, 20, 30, 40, 20)

# Accessing elements
print(t[0])      # First element
print(t[-1])     # Last element

# Slicing
print(t[1:4])    # (20, 30, 40)

# Length of tuple
print(len(t))    # 5

# Count method
print(t.count(20))   # Counts occurrences of 20

# Index method
print(t.index(30))   # Returns index of 30

# Maximum element
print(max(t))        # 40

# Minimum element
print(min(t))        # 10

# Sum of elements
print(sum(t))        # 120

# Sorted tuple (returns list)
print(sorted(t))     # [10, 20, 20, 30, 40]

# Membership operators
print(20 in t)       # True
print(100 not in t)  # True

# Concatenation
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)       # (1, 2, 3, 4)

# Repetition
print(t1 * 3)        # (1, 2, 1, 2, 1, 2)

# Traversing tuple
for i in t:
    print(i)

# Tuple packing
pack = 10, 20, 30
print(pack)          # (10, 20, 30)

# Tuple unpacking
a, b, c = pack
print(a, b, c)       # 10 20 30

# Swapping variables
x = 10
y = 20
x, y = y, x
print(x, y)          # 20 10

# Nested tuple
nested = ((1, 2), (3, 4))
print(nested[1][0])  # 3

# List to Tuple
lst = [1, 2, 3]
tup = tuple(lst)
print(tup)           # (1, 2, 3)

# Tuple to List
new_list = list(tup)
print(new_list)      # [1, 2, 3]


# IMPORTANT NOTE
# Tuple is immutable
# t[0] = 100  # TypeError

# Only two tuple methods:
# 1. count()
# 2. index()

# List Methods:
# append(), extend(), insert(), remove(), pop(),
# clear(), sort(), reverse(), copy(), count(), index()


# ==========================
# TUPLE OPERATIONS
# ==========================

# Indexing
# t[0]

# Negative Indexing
# t[-1]

# Slicing
# t[1:4]

# Concatenation
# t1 + t2

# Repetition
# t * 3

# Membership Operators
# element in t
# element not in t

# Traversal
# for item in t:
#     print(item)

# Tuple Packing
# t = 1, 2, 3

# Tuple Unpacking
# a, b, c = t

# Type Conversion
# list(t)      # Tuple -> List
# tuple(lst)   # List -> Tuple

# Nested Tuple Access
# t[0][1]

# Length of Tuple
# len(t)

# Maximum Element
# max(t)

# Minimum Element
# min(t)

# Sum of Elements
# sum(t)

# Sorting (returns a list)
# sorted(t)

# ==========================
# TUPLE METHODS
# ==========================

# count()
# Returns the number of occurrences of an element
# t.count(20)

# index()
# Returns the index of the first occurrence of an element
# t.index(30)



# Tuple is Immutable
# Cannot add, remove, or modify elements directly

# t[0] = 100      # ❌ Error
# t.append(50)    # ❌ Error
# t.remove(20)    # ❌ Error

