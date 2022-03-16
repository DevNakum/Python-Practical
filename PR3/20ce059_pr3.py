# 20CE059 Dev Nakum

def solve(k,arr1):
    
    l1 = []
    mx = max(arr1)
    
    for i in range(0,mx+1):
        l1.append(0)

    for i in range(0,len(arr1)):
        l1[arr1[i]]+=1
        
    for i in range (0,mx+1):
        # if(l1[i]==1):
        #     print(i)
        if(l1[i]!=k and l1[i]!=0):
            print(i)
         

k = 5

arr1=[1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,3,1,5,6,2]
solve(k,arr1)    
