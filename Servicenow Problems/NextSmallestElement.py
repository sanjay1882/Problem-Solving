arr= [4,1,8,6,33,41,19]
# 1 6 6 19 19 19 0
Min=float('inf')
curr=0
pre=0
for i in range(len(arr)-1,-1,-1):
    curr=arr[i]
    arr[i]=pre
    Min=min(Min,curr)
    pre=Min
print(*arr)

