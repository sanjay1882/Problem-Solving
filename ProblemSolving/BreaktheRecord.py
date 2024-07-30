a=int(input())
list=[]
for i in range(0,a):
    b=int(input())
    list.append(b)

minCount=0
maxCount=0
min=list[0]
max=list[0]
for i in range(1,a):
    if list[i]>max:
        maxCount+=1
        max=list[i]
    elif list[i]<min:
        minCount+=1
        min=list[i]


print("Max",maxCount)
print("Min",minCount)
