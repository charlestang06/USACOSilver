n, q = list(map(int, input().split()))
pre = []
for x in range(n + 1):
    pre.append([])
    for y in range(n + 1):
        pre[x].append(0)

for row in range(n):
    temp = list(input())
    for i in range(len(temp)):
        if temp[i] == '*':
            pre[row + 1][i + 1] = 1

# presum array
for x in range(1, n + 1):
    for y in range(1, n + 1):
        pre[x][y] += pre[x - 1][y] + pre[x][y - 1] - pre[x - 1][y - 1]

for x in range(q):
    coords = list(map(int, input().split()))
    x1 = coords[0]
    y1 = coords[1]
    x2 = coords[2]
    y2 = coords[3]
    print(pre[x2][y2] + pre[x1 - 1][y1 - 1] - pre[x2][y1 - 1] - pre[x1 - 1][y2])
