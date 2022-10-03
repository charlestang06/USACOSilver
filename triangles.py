N = int(input())
pts = []
for x in range(N):
    x_1, y_1 = list(map(int, input().split()))
    pts.append([x_1, y_1])
# fix the code with solution
total = 0
for first in range(len(pts)):
    one = pts[first]
    for second in range(len(pts)):
        if first == second:
            continue
        if pts[second][0] == one[0]:
            two = pts[second]
            y_dist = abs(two[1] - one[1])
            for third in range(len(pts)):
                if (pts[third][1] == two[1] or pts[third][1] == one[1]) and (
                        pts[third][0] != one[0] and pts[third][0] != two[0]):
                    three = pts[third]
                    x_dist = abs(three[0] - one[0])
                    total += x_dist * y_dist
print(int(total / 2))
