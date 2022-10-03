# https://cses.fi/problemset/task/1661

N = int(input())
arr = list(map(int, input().split()))

for i in range(1, N):
    arr[i] += arr[i - 1]

remainder = [0] * (2 * N)
remainder[0] = 1
for i in range(N):
    remainder[(arr[i] % N + N) % N] += 1

final = 0
for i in range(len(remainder)):
    final += remainder[i] * (remainder[i] - 1) / 2

print(int(final))
