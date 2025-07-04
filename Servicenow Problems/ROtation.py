a="not goingz"
T=a.lower()
b=list(T)

flag=False
for i in a:
    if i not in b:
        print(i)
        flag=True
        break
    else:
        flag=False
if not flag:
    print(b)





