from collections import Counter
def findLucky(arr):
    freq = Counter(arr)
    lucky_numbers = [key for key, value in freq.items() if key == value]
    return max(lucky_numbers) if lucky_numbers else -1
arr = [2, 2, 3, 4]
print(findLucky(arr))  
