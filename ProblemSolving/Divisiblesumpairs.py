n=int(input("Enter a Number to create List"))
list=[]
k=int(input("Enter a Number K"))
count=0
for i in range(0,n):
    a=int(input("Enter a list elements"))
    list.append(a)


for i in range(0,n):
    for j in range(i+1,n):
        if (list[i]+list[j]) % k == 0:
            count+=1
print(count)
