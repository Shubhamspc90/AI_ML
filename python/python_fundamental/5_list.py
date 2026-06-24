
# Most Important List Methods
# append()
# extend()
# insert()
# remove()
# pop()
# clear()
# index()
# count()
# sort()
# reverse()
# copy()

# # Most Important Operations
# Indexing
# Slicing
# Concatenation (+)
# Repetition (*)
# Membership (in, not in)
# Traversal
# List Comprehension
# Nested Lists

'''A list is an ordered, mutable (changeable) collection that can store multiple items.'''


fruits = ["apple", "banana", "mango"]
print(fruits)  # ['apple', 'banana', 'mango']

# Creating Lists
nums = [1, 2, 3, 4]
names = ["Shubham", "Varun"]
mixed = [10, "Python", True, 5.5]
empty = []

# Accessing Elements
print("\nAccessing Element through indexing")
fruits = ["apple", "banana", "mango"]
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[-1]) # mango
print(fruits[-2]) # banana

# Slicing
print("\nSlicing")
nums = [10, 20, 30, 40, 50]
print(nums[1:4])  # [20, 30, 40]
print(nums[:3])   # [10, 20, 30]
print(nums[2:])   # [30, 40, 50]
print(nums[::-1]) # [50, 40, 30, 20, 10]

# Updating Elements
print("\nUpdating Elements")
fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"
print(fruits) # ['apple', 'orange', 'mango']

# List Methods
print("\nList Methods\n")

# append()
print("\nappend()") # Adds one element at the end.
nums = [1, 2, 3]
nums.append(4)
print(nums) # [1, 2, 3, 4]

# extend()
print("\nextend()") # Adds multiple elements.
nums = [1, 2]
nums.extend([3, 4, 5])
print(nums)  # [1, 2, 3, 4, 5]

# insert() 
print("\ninsert()") # Insert at a specific position.
nums = [1, 2, 4]
nums.insert(2, 3)
print(nums)  # [1, 2, 3, 4]

# remove()
print("\nremove()") # Removes first occurrence of a value.
nums = [1, 2, 3, 2]
nums.remove(2)
print(nums)  # [1, 3, 2]

# pop()
print("\npop()") # Removes by index.
nums = [10, 20, 30]
nums.pop()
print(nums)

# clear()
print("\nclear()") # Removes all elements.
nums = [1, 2, 3]
nums.clear()
print(nums)  # []

# index()
print("\nindex()") # Returns position of an element.
nums = [10, 20, 30]
print(nums.index(20)) # 1

# count()
print("\ncount()")  #Counts occurrences.
nums = [1, 2, 2, 2, 3]
print(nums.count(2)) # 3

# sort()
print("\nsort()")  #Sorts list in ascending order.
nums = [5, 2, 8, 1]

nums.sort()
print(nums) # [1, 2, 5, 8]
print("Descending: ")
nums.sort(reverse=True)

# reverse()
print("\nreverse()") # Reverses the list.
nums = [1, 2, 3]
nums.reverse()
print(nums)  #[3, 2, 1]

# copy()
print("\ncopy()") # Creates a shallow copy.
a = [1, 2, 3]

b = a.copy()
print(b)  #  [1, 2, 3]

# 6. Built-in Functions Used with Lists

# len()
print("\nlen()")
nums = [1, 2, 3]
print(len(nums)) # 3

# max()
print("\nmax()")
nums = [10, 40, 20]
print(max(nums)) # 40

# min()
print("\nmin()") 
print(min(nums))  # 10

# sum()
print("\nsum()")
nums = [10, 20, 30]
print(sum(nums)) # 60

# sorted()
print("\nsorted()")
nums = [4, 1, 3]
print(sorted(nums)) # [1, 3, 4]

# Operations on Lists

# Concatenation (+)
print("\nConcatenation (+)")
a = [1, 2]
b = [3, 4]
print(a + b)  # [1, 2, 3, 4]

# Repetition (*)
print("\nRepetition (*)")
nums = [1, 2]
print(nums * 3)  # [1, 2, 1, 2, 1, 2]

# Membership
print("\nMembership")
nums = [10, 20, 30]
print(20 in nums)       # True
print(50 not in nums)   # True

# Traversing a List

# Using for loop 
print("\nUsing for loop ")
nums = [10, 20, 30]
for i in nums:
    print(i,end=" ")         # 10 20 30 
    
# Using index
print("\nUsing index")
for i in range(len(nums)):
    print(nums[i],end=" ")   # 10 20 30 
    
# List Comprehension
# Square Numbers
print("\nSquare Numbers")
nums = [1, 2, 3, 4]
square = [i*i for i in nums]
print(square)  # [1, 4, 9, 16]

# Even Numbers
print("\nEven Numbers")
nums = [1, 2, 3, 4, 5, 6]
even = [i for i in nums if i % 2 == 0]
print(even) # [2, 4, 6]

# Nested Lists
print("\nNested Lists")
matrix = [
    [1, 2],
    [3, 4]
]
print(matrix[0][1])  # 2

# List → Tuple
my_list = [1, 2, 3, 4]

my_tuple = tuple(my_list)

print(my_tuple)  #  (1, 2, 3, 4)
print(type(my_tuple))  # <class 'tuple'>