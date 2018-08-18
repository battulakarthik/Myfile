n,m=map(int,input().split())
lst=[int(x) for x in input().split()]
count=0
for i in range(0,n):
	if lst[i]%2!=0:
		count+=1
	if count==m:
		print(lst[i])
		break
	
