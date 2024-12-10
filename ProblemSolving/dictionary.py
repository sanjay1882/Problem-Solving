arr=[32,232,434,1,3,2,34,61]
num_to={}

rank=1

for num in arr:
    num_to[num]=rank
    rank+=1
print(num_to)