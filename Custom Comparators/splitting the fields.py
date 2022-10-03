N = int(input())
x = []
y = []
for i in range(N):
    x_1, y_1 = list(map(int, input().split()))
    x.append(x_1)
    y.append(y_1)

area = (max(x) - min(x)) * (max(y) - min(y))

from functools import cmp_to_key

high = 0

x.sort(key=cmp_to_key(lambda a, b: a - b))
for z in range(2):
    for column in range(N):
        leftX = x[:column + 1]
        rightX = x[column + 1:]
        leftY = y[:column + 1]
        rightY = y[column + 1:]
        if len(leftX) == 0 or len(leftY) == 0:
            areaL = 0
        elif len(rightX) == 0 or len(rightY) == 0:
            areaR = 0
        else:
            areaL = (max(leftX) - min(leftX)) * (max(leftY) - min(leftY))
            areaR = (max(rightX) - min(rightX)) * (max(rightY) - min(rightY))
        high = max(high, area - (areaR + areaL))
    y.sort(key=cmp_to_key(lambda a, b: a - b))

print(high)
