def presum(arr):
    i = len(arr[0])
    j = len(arr)
    pre = [[0 for a in range(i + 1)] for b in range(j + 1)]
    for x in range(1, i + 1):
        for y in range(1, j + 1):
            pre[x][y] = arr[x - 1][y - 1] + pre[x - 1][y] + pre[x][y - 1] - pre[x - 1][y - 1]
    return pre


print(presum([[2, 2], [2, 2]]))
