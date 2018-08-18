n,m=input().split()
count=0
for i in range(0,len(n)):
    if n[i]!=m[i]:
        count+=1
if count==1:
    print("yes")
else:print("no")
