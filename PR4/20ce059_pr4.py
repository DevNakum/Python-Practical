n = int(input())

arr=[]
for i in range(n):
    x = int(input())
    arr.append(x)

s1 = set(arr)
l = len(s1)
l1 = list(s1)
print(l1[l-2])