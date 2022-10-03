N, K = map(int, input().split())

diamonds = []

for i in range(N):
    diamonds.append(int(input()))

diamonds.sort()

# first case of diamonds
p1 = 0
p2 = 1

max_sum = 0
max_p1 = 0
max_p2 = 0

while (p2 < N or p1 < N - 1):
    # max distance
    if (p2 - p1 > max_p2 - max_p1 and diamonds[p2] - diamonds[p1] <= K):
        max_p1 = p1
        max_p2 = p2
    # case 1: difference > K
    if diamonds[p2] - diamonds[p1] > K:
        p1 += 1
    # case 2: difference <= K and second pointer hasn't reached the end
    elif p2 != N - 1 and diamonds[p2] - diamonds[p1] <= K:
        p2 += 1
    # case 3: second pointer reaches end and second pointer reached the end
    else:
        break

# track first case
max_sum += max_p2 - max_p1 + 1

# delete elements from first case
for i in range(max_p1, max_p2):
    diamonds.pop(max_p1)

# second case of diamonds
N = len(diamonds)
p1 = 0
p2 = 1

max_p1 = 0
max_p2 = 0

while (p2 < N or p1 < N - 1):
    # max distance
    if (p2 - p1 > max_p2 - max_p1 and diamonds[p2] - diamonds[p1] <= K):
        max_p1 = p1
        max_p2 = p2
    # case 1: difference > K
    if diamonds[p2] - diamonds[p1] > K:
        p1 += 1
    # case 2: difference <= K and second pointer hasn't reached the end
    elif p2 != N - 1 and diamonds[p2] - diamonds[p1] <= K:
        p2 += 1
    # case 3: second pointer reaches end and second pointer reached the end
    else:
        break

# track first case
max_sum += max_p2 - max_p1 + 1

print(max_sum)
