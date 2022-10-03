N = int(input())
arr = []
for x in range(N):
    arr.append(int(input()))
presum = [0]
for x in range(0, len(arr)):
    presum.append(arr[x] + presum[x])

first = [1000000000000] * 7
last = [0] * 7

for index in range(len(presum)):
    remain = presum[index] % 7
    first[remain] = min(first[remain], index)
    last[remain] = index

diff = []
for x in range(len(first)):
    diff.append(last[x] - first[x])

print(max(diff))
