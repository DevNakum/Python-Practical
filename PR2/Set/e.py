# 5....
# Write a Python program to find the most common elements and their counts from list, tuple, dictionary.


from statistics import mode

# in list
l1 =[1,2,3,4,4,4,4,4,4,5,4,4,6]
print(l1)
print(mode(l1))     # 4

# in tuple
t1 = (1,2,3,4,4,4,4,4,4,5,4,4,6)
print(t1)
print(mode(t1))     # 4