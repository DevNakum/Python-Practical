# 20CE059 Dev Nakum

def swapCase(str):
    ans=""
    for i in str:
        if(i>='a' and i<='z'):
            ans+=i.upper()
        elif(i>='A' and i<='Z'):
            ans+=i.lower()
        else:
            ans+=i
    return ans

str = input("")         #  hackerRank.com presents "Pythonist 2"
print(swapCase(str))        # HACKERrANK.COM PRESENTS "pYTHONIST 2"