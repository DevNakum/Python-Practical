# 1...
# Write a Python script to check whether a given key already exists in a dictionary.

d1 = {1:10, 2:20, 3:30, 4:40}
print("Dictionary is ",d1)
key = int(input("Enter a key : "))

if(key in d1):
    print("key is exists")
else:  
    print("key is not exists")