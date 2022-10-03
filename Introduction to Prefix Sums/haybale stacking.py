N_K = list(map(int, input().split()))
N = N_K[0]
K = N_K[1]

pre = [0] * (N + 1)
for x in range(K):
    temp = list(map(int, input().split()))
    a = temp[0] - 1
    b = temp[1]
    pre[a] += 1
    pre[b] -= 1

for x in range(1, len(pre)):
    pre[x] += pre[x - 1]

pre.sort()
print(pre[int((N + 1) / 2)])
