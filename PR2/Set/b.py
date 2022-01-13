# 2...
# Write a Python program to remove an item from a set if it is present in the set.

s1 = {"Item1","Item2","Item3","Item4"}
print("Before removing Item2 : ",end="")
print(s1)       # {"Item1","Item2","Item3","Item4"}

print("After removing Item2 : ",end="")
s1.remove("Item2")
print(s1)       # {"Item1","Item3","Item4"}