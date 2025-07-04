

def get_usage(N, M, K, arr):
    for i in range(1, M):
        arr.sort()
        arr[0] = arr[0] + 1
    return arr[K - 1]


N = 9
M = 38
K = 3
arr = [2,4,3,5,6,17,8,11,9]
print(arr)
print(get_usage(N, M, K, arr))