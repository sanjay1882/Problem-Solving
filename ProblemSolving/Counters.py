from collections import Counter

a=[3,3,4,5,3,6,8,3,8,8,7,7,7,8,7,7,7]
c=Counter(a)

max=max(dict.values(c))

for i in c:
    if c[i]==max:
        print(i,"repeated",max,"times")


    