#  # Strings in Python
print("Strings in Python")
name = "Shubham"
print(name)  # Shubham

# Access Characters
print("\nAccess Characters")
name = "Python"

print(name[0]) # P
print(name[1]) # y

# Negative Indexing
print("\nNegative Indexing")
name = "Python"

print(name[-1]) # n
print(name[-2]) # o

# String Slicing
print("\nString Slicing")
text = "Artificial Intelligence"

print(text[0:10]) # Artificial
print(text[11:])  # Intelligence
print(text[:10])  # Artificial

# String Methods
print("\nString Methods")

print("\nUpperCase()")
name = "python"
print(name.upper()) # PYTHON

# Lowercase
print("\nLowercase()")
name = "PYTHON"
print(name.lower()) # python

#Capitalize
print("\nCapitalize()")
name="python"
print(name.capitalize()) # Python

# Replace
print("\nReplace()")
text = "I like Java"
print(text.replace("Java", "Python")) # I like Python

# Split
print("\nSplit()")
sentence = "Python is easy"
print(sentence.split())  # ['Python', 'is', 'easy']

# Count
print("\nCount()")
text = "banana"
print(text.count("a"))  # 3
