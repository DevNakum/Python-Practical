# 20CE059 - Dev Nakum


#AIM: Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match. Your task is simple. Given a string, you need to tell if it is a lapindrome. 

# Input: 
# 6 
# gaga 
# abcde 
# rotor 
# xyzxy 
# abbaab 
# ababc 

# Output: 
# YES 
# NO 
# YES 
# YES 
# NO 
# NO

# take input from the user
t = int(input())        

for i in range(t):
    str = input()

    l = len(str)

    # if length is odd number
    if(l%2==1):
        k = int(l/2)
        s1 = str[0:k]
        s2 = str[k+1:]
    
    # if length is even number
    else:
        k = int(l/2)
        s1 = str[0:k]
        s2 = str[k:]

    # sorrt the s1 and s2
    cs1 = sorted(s1)
    cs2 = sorted(s2)

    # compare the both string it is same or not
    if(cs1==cs2):
        print("YES")
    else:
        print("NO")