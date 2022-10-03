# http://usaco.org/index.php?page=viewproblem2&cpid=1064

N = int(input())
original = []

east_cows = []
north_cows = []
# each cow is [x, y, number of cows stopped, isStopped boolean)

for i in range(N):
    direction, x, y = map(str, input().split())
    original.append([int(x), int(y)])
    if direction == "E":
        east_cows.append([int(x), int(y), 0, False])
    else:
        north_cows.append([int(x), int(y), 0, False])

# sort east facing cows from south to north
east_cows.sort(key=lambda x: x[1])

# sort north facing cows from east to west
north_cows.sort(key=lambda x: x[0])

for ncow in north_cows:
    for ecow in east_cows:
        # if already stopped, break / continue
        if ecow[3]:
            continue
        if ncow[3]:
            break
        # ecow must be upper left of ncow
        if (ecow[0] < ncow[0] and ecow[1] > ncow[1]):
            print("hi")
            # two possibilities
            # possibility 1: ecow stops ncow
            if (ncow[0] - ecow[0] < ecow[1] - ncow[1]):
                ecow[2] += ncow[2] + 1
                ncow[3] = True
            # possibility 2: ncow stops ecow
            elif (ecow[1] - ncow[1] < ncow[0] - ecow[0]):
                ncow[2] += ecow[2] + 1
                ecow[3] = True
            # no collision
            else:
                continue

output = [0] * N
for ncow in north_cows:
    output[original.index([ncow[0], ncow[1]])] = ncow[2]

for ecow in east_cows:
    output[original.index([ecow[0], ecow[1]])] = ecow[2]

for a in output:
    print(a)
