N, target = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

for p1 in range(0, N - 2):
    p2 = p1 + 1
    p3 = N - 1

    sum = nums[p1] + nums[p2] + nums[p3]

    while sum != target:
        if sum < target:
            p2 += 1
        if sum > target:
            p3 -= 1
        sum = nums[p1] + nums[p2] + nums[p3]
    if sum == target:
        print(f"{nums[p1]} {nums[p2]} {nums[p3]}")
        exit()

print("IMPOSSIBLE")
