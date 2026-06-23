"""A Set is an unordered, mutable collection of unique elements."""
s = {10, 20, 30, 40}
print(s)  # {40, 10, 20, 30}

# Characteristics of Set
#  Unordered
#  Mutable
#  No Duplicate Values
#  Fast Membership Testing

'''
add()
update()
remove()
discard()
pop()
clear()
copy()

union()
intersection()
difference()
symmetric_difference()

intersection_update()
difference_update()
symmetric_difference_update()

issubset()
issuperset()
isdisjoint()
'''

s = {1, 2, 2, 3, 3, 4}
print(s)  # {1, 2, 3, 4}

#Empty Set
s = set()      # Correct
# s = {}       # Dictionary

# Accessing Elements
s = {10, 20, 30}
# print(s[0])   # Error ,Sets do not support indexing.

# Traversing a Set
s = {10, 20, 30}

for i in s:
    print(i, end=" ")  # 10 20 30

# SET METHODS

#  add()   Adds a single element.
print("\nadd()") 
s = {1, 2, 3}
s.add(4)  
print(s)  # {1, 2, 3, 4}

# update()   Adds multiple elements.
print("\nupdate()")
s = {1, 2}
s.update([3, 4, 5]) 
print(s)  # {1, 2, 3, 4, 5}

# remove() Removes an element.
print("\nremove()")
s = {1, 2, 3}
s.remove(2)  #  Error if element does not exist.
print(s)  # {1, 3}

# discard()  Removes element safely.
print("\ndiscard()")
s = {1, 2, 3}
s.discard(5)
print(s)  # {1, 2, 3}

# pop()  Removes and returns a random element.
print("\npop()")
s = {10, 20, 30}
print(s.pop())  # 10

# clear()  Removes all elements.
print("\nclear()")
s = {1, 2, 3}
s.clear()
print(s)  # set()

# copy()  Creates a shallow copy.
print("\ncopy()")
s = {1, 2, 3}
new_s = s.copy()
print(new_s)  # {1, 2, 3}



# SET OPERATIONS, METHODS & CONVERSIONS
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# UNION
print("Union")
print(A.union(B))  # {1, 2, 3, 4, 5, 6}
print(A | B)  # {1, 2, 3, 4, 5, 6}

# INTERSECTION
print("\nIntersection")
print(A.intersection(B))  # {3, 4}
print(A & B)  # {3, 4}

# DIFFERENCE
print("\nDifference")
print(A.difference(B))  # {1, 2}
print(A - B)  # {1, 2}

# SYMMETRIC DIFFERENCE
print("\nSymmetric Difference")
print(A.symmetric_difference(B))  # {1, 2, 5, 6}
print(A ^ B)  # {1, 2, 5, 6}

# INTERSECTION UPDATE
print("\nIntersection Update")
A = {1, 2, 3}
B = {2, 3, 4}
A.intersection_update(B)
print(A)  # {2, 3}

# DIFFERENCE UPDATE
print("\nDifference Update")
A = {1, 2, 3}
B = {2, 3}
A.difference_update(B)
print(A)  # {1}

# SYMMETRIC DIFFERENCE UPDATE
print("\nSymmetric Difference Update")
A = {1, 2, 3}
B = {3, 4}
A.symmetric_difference_update(B)
print(A)  # {1, 2, 4}

# ISSUBSET
print("\nissubset")
A = {1, 2}
B = {1, 2, 3}
print(A.issubset(B))  # True

# ISSUPERSET
print("\nissuperset")
A = {1, 2, 3}
B = {1, 2}
print(A.issuperset(B))  # True

# ISDISJOINT
print("\nisdisjoint")
A = {1, 2}
B = {3, 4}
print(A.isdisjoint(B))  # True

# BUILT-IN FUNCTIONS
print("\nBuilt-in Functions")

print("Length:", len({1, 2, 3}))  # Length: 3
print("Maximum:", max({10, 20, 30}))  # Maximum: 30
print("Minimum:", min({10, 20, 30}))  # Minimum: 10
print("Sum:", sum({10, 20, 30}))  # Sum: 60
print("Sorted:", sorted({30, 10, 20}))  # Sorted: [10, 20, 30]

# MEMBERSHIP OPERATORS
print("\nMembership Operators")
s = {10, 20, 30}
print(20 in s)  #  True
print(100 not in s)  # True

# TYPE CONVERSION
print("\nType Conversion")

# List -> Set
lst = [1, 2, 2, 3]
s = set(lst)
print("List to Set:", s)  # List to Set: {1, 2, 3}

# Set -> List
lst2 = list(s)
print("Set to List:", lst2)  # Set to List: [1, 2, 3]

# Set -> Tuple
t = tuple(s)
print("Set to Tuple:", t)  # Set to Tuple: (1, 2, 3)

# Tuple -> Set
s2 = set((1, 2, 3))
print("Tuple to Set:", s2)  # Tuple to Set: {1, 2, 3}




















'''
# Union
A | B

# Intersection
A & B

# Difference
A - B

# Symmetric Difference
A ^ B

# Membership
in
not in

# Traversal
for i in s

# Conversion
list()
tuple()
set()
'''







