from collections import deque
a=[4,2,5,6,-1]

c=0
d=deque(a)
while a:
    if d[0]==a[0]:
        d.popleft()
        c+=1
    else:
        d.extend(d.popleft())



print(c)

