# 3....
# Write a Python program to sum all the items in a dictionary.

d1 = {
    "key1" : 10,
    "key2" : 20,
    "key3" : 30
}


l1 = []
for i in d1:
    l1.append(d1[i])
ans = sum(l1)
print(ans)      # 10+20+30 = 60