# http://www.usaco.org/index.php?page=viewproblem2&cpid=738

N = int(input())

cows = []

for i in range(N):
    x, y = map(int, input().split())
    cows.append([x, y])

cows.sort(key=lambda cow: cow[1])

p1 = 0
p2 = N - 1

max_sum = 0

while (p1 < p2):
    p1_cows = cows[p1][0]
    p2_cows = cows[p2][0]

    max_sum = max(max_sum, cows[p1][1] + cows[p2][1])

    # case 1: latter cow has more cows
    if (p2_cows > p1_cows):
        cows[p2][0] -= p1_cows
        p1 += 1
    # case 2: former cow has more cows
    elif (p1_cows > p2_cows):
        cows[p1][0] -= p2_cows
        p2 -= 1
    # case 3: same number of cows
    else:
        p1 += 1
        p2 -= 1

print(max_sum)
