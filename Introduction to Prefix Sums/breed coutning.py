# http://www.usaco.org/index.php?page=viewproblem2&cpid=572

N, Q = list(map(int, input().split()))

holsteins = []
guernseys = []
jerseys = []

cows = []
for i in range(N):
    cows.append(int(input()))

for i in range(len(cows)):
    if cows[i] == 1:
        holsteins.append(1)
        guernseys.append(0)
        jerseys.append(0)
    elif cows[i] == 2:
        holsteins.append(0)
        guernseys.append(1)
        jerseys.append(0)
    elif cows[i] == 3:
        holsteins.append(0)
        guernseys.append(0)
        jerseys.append(1)

for i in range(1, N):
    holsteins[i] += holsteins[i - 1]
    guernseys[i] += guernseys[i - 1]
    jerseys[i] += jerseys[i - 1]

holsteins.insert(0, 0)
guernseys.insert(0, 0)
jerseys.insert(0, 0)

for i in range(Q):
    a, b = list(map(int, input().split()))
    final = [holsteins[b] - holsteins[a - 1], guernseys[b] - guernseys[a - 1], jerseys[b] - jerseys[a - 1]]
    print(f'{final[0]} {final[1]} {final[2]}')
