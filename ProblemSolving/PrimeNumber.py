def PrimeNumber(num):
    if num<=1:
        return False
    for i in range(2,(num//2)):
        if (num%i)==0:
            return False
    return True




def Iterate_Prime_Num(start,end):
    for i in range(start,end+1):
        if PrimeNumber(i):
            print(i,end=' ')
        

    







Iterate_Prime_Num(1,100)