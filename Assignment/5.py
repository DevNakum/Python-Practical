# arithmetic exception
try:    
    a = int(input("Enter a:"))    
    b = int(input("Enter b:"))    
    c = a/b  
    print("a/b = %d"%c)    
# Using Exception with except statement. If we print(Exception) it will return exception class  
except Exception:    
    print("can't divide by zero")    
    print(Exception)  
else:    
    print("Hi I am else block")


# IO exception
try:    
    #this will throw an exception if the file doesn't exist.     
    fileptr = open("file.txt","r")    
except IOError:    
    print("File not found")    
else:    
    print("The file opened successfully")    
    fileptr.close()

# file exception
try:    
    fileptr = open("file2.txt","r")      
    try:    
        fileptr.write("Hi I am good")    
    finally:    
        fileptr.close()    
        print("file closed")    
except:    
    print("Error")


# # nameerror exception
# def geek_message():
# 	try:
# 		geek = "GeeksforGeeks"
# 		return geeksforgeeks
# 	except NameError:
# 		return "NameError occurred. Some variable isn't defined."

# print(geek_message())