N = list(map(int, input().split()))
arr = list(map(int, input().split()))

for x in range(1, len(arr)):
    arr[x] += arr[x - 1]

max_sum = arr[0]
min_sum = 0
running_sum = 0
for x in arr:
    max_sum = max(max_sum, x - min_sum)
    min_sum = min(min_sum, x)
print(max_sum)
