a=[4,2,5,1,3,1,7,6]

a=[1,2,1,5,6,1]
def Wave(a):
    if len(a)<=2 :
        return True

    for i in range(1,len(a)-1,2):
        if a[i-1]>a[i]<a[i+1] or a[i-1]<a[i]>a[i+1] :
            continue
        else:
            return False
    return True

print(Wave(a))