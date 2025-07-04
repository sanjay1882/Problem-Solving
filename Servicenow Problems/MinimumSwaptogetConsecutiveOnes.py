arr = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0]


total=sum(arr)
Min=float('inf')
for i in range((len(arr)-total)+1):
    Min=min(Min,total-sum(arr[i:i+total]))
print(Min)
