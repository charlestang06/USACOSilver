lengths = list(map(int, input().split()))
arr = list(map(int, input().split()))

presum = [0]
for x in range(0, len(arr)):
    presum.append(arr[x] + presum[x])

for x in range(lengths[1]):
    temp = list(map(int, input().split()))
    sum = presum[temp[1]] - presum[temp[0]]
    print(sum)
