arr=[32,232,434,1,3,2,34,61]
num_to={}
nums=sorted(arr) #sort set and convert to list


for itr,num in enumerate(nums,1):
    num_to[num]=itr



for i in range(len(arr)):
    arr[i]=num_to[arr[i]]

print(arr)