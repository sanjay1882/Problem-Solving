a=[1,1,5,6,7,3,3,3,3,3,5,9,9,9,9]
f=a[0]
c=0
Max=0
for i in range(len(a)):
    if a[i]!=f:
        f=a[i]
        Max=max(c,Max)
        c=1
    else:
        c+=1


print(Max,f)

