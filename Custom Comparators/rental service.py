N, M, R = list(map(int, input().split()))
gals = []
stores = []
rents = []
for x in range(N):
    gals.append(int(input()))
for x in range(M):
    gal, cent = list(map(int, input().split()))
    stores.append([gal, cent])
for x in range(R):
    rents.append(int(input()))

gals.sort()
stores.sort(key=lambda x: x[1])
rents.sort()
for x in range(R - 2, -1, -1):
    rents[x] += rents[x + 1]

high = rents[R - min(N, R)]
sold = 0
currStore = 0

for x in range(N - 1, -1, -1):
    while gals[x] > 0 and currStore < M:
        if stores[currStore][0] <= gals[x]:
            sold += stores[currStore][1] * stores[currStore][0]
            gals[x] -= stores[currStore][0]
            currStore += 1
        else:
            sold += stores[currStore][1] * gals[x]
            stores[currStore][0] -= gals[x]
            gals[x] = 0
    if x == 0:
        high = max(high, sold)
    else:
        high = max(high, sold + rents[R - min(x, R)])
print(high)
