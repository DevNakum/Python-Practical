from numpy import sort


str = input()   #take input from the user

freq={}
for i in str:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
    
print(freq)