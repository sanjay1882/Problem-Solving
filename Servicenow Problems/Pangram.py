a="hello"
b=set(a)
flag=False
for i in range(97,122+1):
    if chr(i) not in b:
        print("Not Pangram")

        flag=False