# 3..
# Write a Python program to add an item in a tuple.

t1 = ("Item1","Item2","Item3","Item4")
print("Before adding Item")
print(t1)       # ('Item1', 'Item2', 'Item3', 'Item4')
print("After adding Item")
l1 = list(t1)       # convert tuple into list so we can add the element 
l1.append("Item5")
t1 = tuple(l1)      # convert list into tuple
print(t1)       # ('Item1', 'Item2', 'Item3', 'Item4', 'Item5')