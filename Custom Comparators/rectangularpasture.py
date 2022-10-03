# http://www.usaco.org/index.php?page=viewproblem2&cpid=1063

# input
N = int(input())
coords = []
for i in range(N):
    coords.append(list(map(int, input().split())))

# sort by x-value
coords.sort(key=lambda x: x[0])
# change x-value into rank order
for i in range(N):
    coords[i][0] = i

# sort by y-value
coords.sort(key=lambda y: y[1])
# change y-value into rank order
for i in range(N):
    coords[i][1] = i

# sort by x-value for processing
coords.sort(key=lambda x: x[0])

# prefix sum array
preSum = []
for i in range(N):
    preSum.append([0] * N)

# input coordiantes
for i in range(N):
    preSum[coords[i][0]][coords[i][1]] = 1

# helper y-coordinate set for prefix sum
helper = {-1}

# presum
for i in range(N):
    for j in range(N):
        tr = False
        if preSum[i][j] == 1:
            tr = True
        if (j != 0):
            preSum[i][j] += preSum[i][j - 1]
        if (j in helper):
            preSum[i][j] += 1
        if tr:
            helper.add(j)

# find answer
count = 0
for i in range(N):
    for j in range(i + 1, N):
        yMax = max(coords[i][1], coords[j][1])
        yMin = min(coords[i][1], coords[j][1])
        topArea = 0
        if i == 0:
            topArea = preSum[j][N - 1] - preSum[j][yMax] + 1
        else:
            topArea = preSum[j][N - 1] - preSum[j][yMax] - preSum[i - 1][N - 1] + preSum[i - 1][yMin] + 1

        bottomArea = 0
        if yMax == 0:
            bottomArea = 1
        else:
            if i == 0:
                bottomArea = preSum[j][yMin - 1] + 1
            else:
                bottomArea = preSum[j][yMin - 1] - preSum[i - 1][yMin - 1] + 1
        count += topArea * bottomArea

# account for sets of single cows and empty set
count += N + 1

print(count)
