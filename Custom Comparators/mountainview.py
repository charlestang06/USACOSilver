# http://www.usaco.org/index.php?page=viewproblem2&cpid=896

N = int(input())
mountains = []

for i in range(N):
    x, y = map(int, input().split())
    # add start and end coordinates of mountain
    mountains.append((x - y, x + y))

# sort by
mountains.sort(key=lambda x: (x[0], -1 * x[1]))

answer = 1
high = mountains[0][1]
for i in range(1, N):
    cur = mountains[i][1]
    if cur > high:
        high = cur
        answer += 1

print(answer)
