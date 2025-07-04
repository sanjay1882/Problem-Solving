def compareTriplets(a, b):
    # Write your code here
    al=0
    bob=0
    for a,b in zip(a,b):
        if a>b:
            al+=1
        elif b>a:
            bob+=1

    
    return al,bob

a = [1, 2, 3]
b = [3, 2, 1]

print(compareTriplets(a, b))