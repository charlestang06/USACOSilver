N = int(input())
arr = [0] * 1000000
for x in range(N):
    in_, out_ = list(map(int, input().split()))
    arr[in_] += 1
    arr[out_] -= 1

for x in range(1, len(arr)):
    arr[x] += arr[x - 1]

print(max(arr))
