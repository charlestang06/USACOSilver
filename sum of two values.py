N, sum = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()

# need to fix??

i, j = 0, N - 1
for x in range(2 * N):
    if i == j:
        print('IMPOSSIBLE')
        exit()
    if nums[i] + nums[j] == sum:
        print(f'{i} {j}')
        exit()
    elif nums[i] + nums[j] < sum:
        i += 1
    else:
        j -= 1
print('IMPOSSIBLE')
