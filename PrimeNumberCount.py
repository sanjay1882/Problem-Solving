import math
def Prime(a):
    if a<=1:
        return 1
    for i in range(2,int(math.sqrt(a))+1):
        if (a%i)==0:
            return False
    return True

Sum=0
List=[]
a=40
for i in range(2,a):
    if Prime(i):
        List.append(i)
Min=0
print(List)
for i in range(len(List)):

    for j in range(i,len(List)):

        C+=1
        if  List[i]+List[j]==a:
            Min=min(Min,C)


print(Min)



