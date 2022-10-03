# http://www.usaco.org/index.php?page=viewproblem2&cpid=992


N, M = map(int, input().split())  # N = cow #, M = number of wormholes
locations = list(map(int, input().split()))  # cow locations, index+1 is cow number
wormholes = []
for i in range(M):
    wormholes.append(list(map(int, input().split())))
wormholes.sort(key=lambda hole: hole[2])
print(wormholes)
low = -1
for i in range(len(wormholes)):
    ind1 = min(wormholes[i][0] - 1, wormholes[i][1] - 1)
    ind2 = max(wormholes[i][0] - 1, wormholes[i][1] - 1)
    width = wormholes[i][2]
    if (locations[ind1] <= locations[ind2]):
        continue
    else:
        locations[ind1], locations[ind2] = locations[ind2], locations[ind1]
        low = width
print(locations)
print(low)
