N, M = map(int, input().split())
spotty = []
plain = []
for x in range(N):
    spotty.append(list(input()))
for x in range(N):
    plain.append(list(input()))

# choose one, two, three, all pairs must be distinct
counter = 0
for first in range(0, M - 2):
    for second in range(first + 1, M - 1):
        for third in range(second + 1, M):
            temp_spotty = []
            temp_plain = []
            possible = True
            for x in range(N):
                temp_spotty.append([spotty[x][first], spotty[x][second], spotty[x][third]])
                temp_plain.append([plain[x][first], plain[x][second], plain[x][third]])
            for y in temp_spotty:
                if y in temp_plain:
                    possible = False
                    break
            if possible == True:
                counter += 1

print(counter)
