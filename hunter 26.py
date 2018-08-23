n=int(input())
if n>=1 and n<=10000:
    lst=[int(x) for x in input().split()]
    for i in range(n-1,-1,-1):
        if i>0:
            k="->"
        else:k=''
        print(lst[i],end=k)
