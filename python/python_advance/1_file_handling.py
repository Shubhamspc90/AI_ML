# File Handling in Python
"""File handling allows you to create, read, write, append, and manage files in Python."""

# 1. Opening a File  (Use the open() function)
file =open("spc.txt","r")

file.close()

# Reading file  (Read Entire File)
print("\nRead Entire File:")
file =open("spc.txt","r")
content =file.read()
print(content)

file.close()

#  Read One Line
print("\nRead One Line:")
file= open ("spc.txt","r")
print(file.readline())
file .close()

# Read All Lines
print("\nRead All Lines")
file = open("spc.txt","r")
content=file.readlines()  # or  print(file.readlines()) 
print(content)
file.close()

######################################

# 3. Writing to a File
print("\nWriting to a File")
file =open("vcp.txt","w")
content = """
Hello
Welcome to Python
File Handling
"""
file.write(content)
file. close()

#######################################

# 4. Appending Data
print("\nAppending Data")
file=open("vcp.txt","a")
content="I am going to append the content into vcp.txt"
file.write(content)

file .close()

##########################################
# 5. Using with Statement (Recommended)

print("\nThe with statement automatically closes the file.")
with open("spc.txt","r") as file:
    print(file.read())
    
    
#############################################
# Writing with with:
print("\nWriting with with:")
with open("dsp.txt","w") as f:
    content=" i am content of dsp.txt file"
    f.write(content)
    
    
##############################################
# 6. Checking if a File Exists
print("\nChecking if a File Exists")
import os

if os.path.exists("spc.txt"):
    print("File exists")
else:
    print("File does not exist")
    
##################################################

# 7. Deleting a File
print("\nDeleting a File")
import os
os.remove("dsp.txt")
print("file removed successfully.")

###################################################

# 8. Example Program
# Writing to a file
with open("student.txt", "w") as file:
    file.write("John\n")
    file.write("Alice\n")

# Reading from a file
with open("student.txt", "r") as file:
    print(file.read())
    
