nm=[x for x in input().split()]
for i in range(0,len(nm)):
    if i<len(nm)-1:
        k=' '
    else:k=''
    print(nm[i].capitalize(),end=k)
