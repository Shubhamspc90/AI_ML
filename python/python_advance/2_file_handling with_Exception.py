# 1. Reading a File with Exception Handling
try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("file does no exist")
    
except PermissionError:
    print("permission denied")

except Exception as e:
    print("an error occured",e)
    

##############################################
# 2. Writing to a File with Exception Handling
try:
    with open("ssp.text","w") as file:
        file.write("hello ssp file ")
    
    print("Data inserted succesfully")

except Exception as e:
    print("an erroe occured",e)
    
################################################
# 3. Appending to a File with Exception Handling
try:
    with open("ssp.txt","a") as f:
        f.write("i am appended content")
        f.write("i like to learn exception handling")
    print("data appended sucessfully.")

except Exception as e :
    print("an error!",e)
    
#################################################
# 4. Deleting a File with Exception Handling
import os
try:
    os.remove("ssp.text")
    print("file removed succesfully.")
    
except FileNotFoundError:
    print("file does not exist")

except PermissionError:
    print("Permission dennied.")
   
except Exception as e:
    print("an error!",e)
    
###################################################
# 5. Complete File Handling Program
try:
    with open("demo.txt","w") as ff:
        ff.write("hello, I'm demo file ")
    print("demo file created successfully.")
    
    with open("demo.txt","r") as ff:
        print("reading demo file completed")
        print(ff.read())
        
    with open("demo.txt","a") as ff:
        ff.write("I am going to appned my self in demo file. ")
        
    with open("demo.txt","a") as ff:
        print("updated content")
        print(ff.read())
        
except FileNotFoundError:
    print("file not found!")

except PermissionError:    
    print("permission denied!")
    
except Exception as e:
    print("error!",e)
    
finally:
    print("Program Completed.")

######################################################

try:
    with open("sample.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("File not found")

except Exception as e:
    print(e)