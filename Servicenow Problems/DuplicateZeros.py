a=[0,12,3,0,9,2,0,82,32,22,2]


def DuplicateZeros(a):
    s=0
    e=len(a)-1
    while s<e:
        if a[s]==0:
            a.insert(s,0)
            a.pop()
            s+=2
        else:
            s+=1



DuplicateZeros(a)
print(a)