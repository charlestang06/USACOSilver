# http://www.usaco.org/index.php?page=viewproblem2&cpid=691

# input
# arr for hoof, paper and scissors
# presum the array
# go through each point, and determine max of games at point -- max of first is what, max of second half is what, calculate total games won
# store that in another final array
# max of the final array

N = int(input())
h = [0]
p = [0]
s = [0]
for i in range(N):
    temp = input()
    if temp == 'S':
        h.append(1)
        p.append(0)
        s.append(0)
    if temp == 'H':
        p.append(1)
        s.append(0)
        h.append(0)
    if temp == 'P':
        s.append(1)
        p.append(0)
        h.append(0)

for i in range(1, N + 1):
    p[i] += p[i - 1]
    h[i] += h[i - 1]
    s[i] += s[i - 1]

running_max = max(p[N], s[N], h[N])

for split in range(1, N):
    h_p = h[split] + p[N] - p[split]
    h_s = h[split] + s[N] - s[split]
    s_p = s[split] + p[N] - p[split]
    s_h = s[split] + h[N] - h[split]
    p_s = p[split] + s[N] - s[split]
    p_h = p[split] + h[N] - h[split]
    running_max = max(running_max, h_p, h_s, s_p, s_h, p_s, p_h)

print(running_max)
