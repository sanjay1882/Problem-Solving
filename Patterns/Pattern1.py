#square pattern
for i in range(5):                              
    for j in range(5):                          #***
        print("*",end='')                       #***
    print()                                     #***

for i in range(3):
    for j in range(3):
        if j==2 :
            print(" *",end=' ')
        else:
            print(" ",end=' ')
    print(" ")