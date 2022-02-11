# 20CE059 - Dev Nakum

# AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification. 
# Sample Input 
# 4 
# bcdef 
# abcdefg 
# bcde 
# bcdef 
# Sample Output 
# 3 
# 2 1 1 

# take input from the user
t = int(input())

# create the list
words = []
for i in range(t):
    str = input()
    words.append(str)

# convert into set so that easily count the distinct value
ans = set(words)
print(len(ans))

ele = {}
for i in words:

    # if string is same add the value 
    if i in ele:
        ele[i]+=1
    else:
        ele[i]=1

for key,value in ele.items():
    print(value,end=" ")