N_K = list(map(int, input().split()))
N = N_K[0]
K = N_K[1]

pre = []
for x in range(1001):
    pre.append([])
    for y in range(1001):
        pre[x].append(0)

for x in range(N):
    coords = list(map(int, input().split()))
    x1 = coords[0]
    y1 = coords[1]
    x2 = coords[2]
    y2 = coords[3]
    pre[x1][y1] += 1
    pre[x1][y2] -= 1
    pre[x2][y1] -= 1
    pre[x2][y2] += 1

counter = 0
for x in range(0, 1001):
    for y in range(0, 1001):
        if x > 0: pre[x][y] += pre[x - 1][y]
        if y > 0: pre[x][y] += pre[x][y - 1]
        if x > 0 and y > 0: pre[x][y] -= pre[x - 1][y - 1]
        if pre[x][y] == K:
            counter += 1
print(counter)
