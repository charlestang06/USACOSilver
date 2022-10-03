# https://codeforces.com/gym/102951/problem/D

N, Q = map(int, input().split())

updates = []  # inputs [l, r, v]
queries = []  # queries [l, r]
indices = []  # sorted list of special indices
difference_array = []
widths = [0] * 400005
interval_value = [0] * 400005
presums = [0] * 400005


def binary_search(list, target):
    start = 0
    end = len(list) - 1
    while (start <= end):
        mid = (start + end) // 2
        if (list[mid] > target):
            end = mid - 1
        elif (list[mid] < target):
            start = mid + 1
        else:
            return mid


for i in range(N):
    values = list(map(int, input().split()))
    updates.append(values)
    indices.append(values[0])
    indices.append(values[1])

for i in range(Q):
    values = list(map(int, input().split()))
    queries.append(values)
    indices.append(values[0])
    indices.append(values[1])

indices = sorted(list(dict.fromkeys(indices)))
difference_array = [0] * (len(indices) + 1)

for i in range(len(updates)):
    l_index = binary_search(indices, updates[i][0])
    r_index = binary_search(indices, updates[i][1])
    v = updates[i][2]
    difference_array[l_index] += v
    difference_array[r_index] -= v

for i in range(len(indices) - 1):
    widths[i + 1] = indices[i + 1] - indices[i]

for i in range(1, len(indices)):
    interval_value[i] = interval_value[i - 1] + difference_array[i]

for i in range(1, len(indices)):
    presums[i] = presums[i - 1] + interval_value[i] * widths[i]

for i in range(Q):
    print(presums[binary_search(indices, queries[i][1])] - presums[binary_search(indices, queries[i][0])])

print(presums[0:11])
