# http://www.usaco.org/index.php?page=viewproblem2&cpid=835

N = int(input())

cows = list(map(int, input().split()))
cows.sort(reverse=True)

for i in range(len(cows)):
    if cows[i] < i:
        print(i)
        exit()
print(N)
