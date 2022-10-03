# http://www.usaco.org/index.php?page=viewproblem2&cpid=786

# class to hold the time start/end of each interval + the cow ID
class State:
    def __init__(self, a, b):
        self.time = a
        self.index = b


N = int(input())
lifeguards = []
currently_working = set()
for i in range(N):
    input_ = list(map(int, input().split()))
    # create State for start of interval
    lifeguards.append(State(input_[0], i))
    # create State for end of interval
    lifeguards.append(State(input_[1], i))

# sort
lifeguards.sort(key=lambda x: x.time)

# total time covered by any cow
actualCover = 0

# array tracking minutes worked by each cow IF ITS ON ITS OWN
alone = [0] * N

# previous time to work with
last = 0

for state in lifeguards:
    # if cow is working by itself, track the minutes it works by itself in the alone array
    if (len(currently_working) == 1):
        alone[list(currently_working)[0]] += state.time - last
    # if there are working cows, add time to totalTime
    if (len(currently_working) > 0):
        actualCover += state.time - last
    # if the cow ID is already working (meaning you reached the end of the cow interval), remove the cow from working
    if (state.index in currently_working):
        currently_working.remove(state.index)
    # else, you reacehd the start of the cow interval, so add the cow to currently working
    else:
        currently_working.add(state.index)
    # update last time
    last = state.time

# maximum total time
ret = 0
for i in alone:
    # find maximum time still covered when remove one
    ret = max(ret, actualCover - i)

print(ret)
