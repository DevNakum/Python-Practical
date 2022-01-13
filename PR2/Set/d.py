# 4...
#  Write a Python program to find maximum and the minimum value in a set.

from typing import Counter
s1 = {1,2,3,4,5,4,4,6}

print("Set is ",s1)
print("maximum value is",max(s1))       # 6
print("minimum value is",min(s1))       # 1
print(Counter(s1))      # Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})