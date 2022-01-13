# 3...
# Write a Python program to create an intersection, Union, difference of sets.

# union 
s1 = {"Item1","Item2","Item3","Item4"}
s2 = {"Item5","Item2","Item3","Item6"}
s3 = s1.union(s2)
print("Union of s1 and s2 is",s3)       # {'Item6', 'Item1', 'Item2', 'Item3', 'Item5', 'Item4'}


# intersection
s1 = {"Item1","Item2","Item3","Item4"}
s2 = {"Item5","Item2","Item3","Item6"}
s3 = {"Item5","Item2","Item1","Item6"}
s4 = s1.intersection(s2,s3)
print("intersection of s1 , s2 and s3 is",s4)       # {'Item2'}


# difference
s1 = {"Item1","Item2","Item3","Item4"}
s2 = {"Item5","Item2","Item3","Item6"}
s3 = s1.difference(s2)
print("difference of s1 and s2 is",s3)      # {'Item4', 'Item1'}
