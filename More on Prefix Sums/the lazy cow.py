# http://www.usaco.org/index.php?page=viewproblem2&cpid=416

N, K = list(map(int, input().split()))
field = []
for i in range(2 * N):
    arr = [0] * (2 * N)
    field.append(arr)

# convert to diagonal matrix
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        field[i + j][N - i + j - 1] = temp[j]

for i in range(2 * N):
    for j in range(2 * N):
        if i >= 1:
            field[i][j] += field[i - 1][j]
        if j >= 1:
            field[i][j] += field[i][j - 1]
        if i >= 1 and j >= 1:
            field[i][j] -= field[i - 1][j - 1]


def bound(x):
    return max(min(x, 2 * N - 1), 1)


max_sum = 0
for i in range(2 * N):
    for j in range(2 * N):
        # max sum of (2K+1 by 2K+1 subarray)
        # corners
        bi = bound(i + 2 * K + 1)
        bj = bound(j + 2 * K + 1)
        si = i
        sj = j

        # edges
        lr = field[bi][bj]
        ur = field[si][bj]
        ll = field[bi][sj]
        ul = field[si][sj]
        max_sum = max(max_sum, lr - ll - ur + ul)

# for row in field:
# print(" ".join(map(str, row)))

print(max_sum)
