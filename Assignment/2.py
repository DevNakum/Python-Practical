import statistics as s

l1=[10,50,80,70,49,23,11,4]

mn = min(l1)        # find minimum number
mx = max(l1)        # find maximum number
men = s.mean(l1)        # find mean value
sd = s.stdev(l1)        # find standard devi ation,
vr = s.variance(l1)     # find variance of nu mber

print(l1)
ans =[round(mn,2),round(mx,2),round(men,2),round(sd,2),round(vr,2)]
print(ans)