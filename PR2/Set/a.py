# 1...
# Write a Python program to add member(s) in a set and clear a set

s1 = {"Item1","Item2","Item3","Item4"}
print("Before adding Item5")
print(s1)       #{'Item1', 'Item2', 'Item3', 'Item4'}

s1.add("Item5")
print("After adding Item5")
print(s1)       # {'Item2', 'Item3', 'Item1', 'Item5', 'Item4'}

s1.clear()
print("After Clear a set")
print(s1)       # set()