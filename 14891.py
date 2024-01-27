import sys
from collections import deque

cogs = [deque(), deque(), deque(), deque()]

for i in range(4):
    tmp = sys.stdin.readline().strip()
    for t in tmp:
        cogs[i].append(t)

N = int(sys.stdin.readline().strip())


def turnClockWise(cog):
    cog.appendleft(cog.pop())


def turnCounterClockWise(cog):
    cog.append(cog.popleft())

def calc(cogs):
    result = 0
    for i in range(4):
        if cogs[i][0] == '1':
            result += 2**i
    return result

for _ in range(N):
    idx, dir = map(int, sys.stdin.readline().split())
    idx -= 1

    selected_cog = []
    selected_cog.append((idx,dir))

    left = cogs[idx][2]
    right = cogs[idx][6]

    t_dir = dir

    for i in range(idx - 1, -1, -1):
        if cogs[i][2] != right:
            if t_dir == 1:
                t_dir = -1
            else :
                t_dir = 1
            selected_cog.append((i, t_dir))
            right = cogs[i][6]
        else:
            break

    t_dir = dir

    for i in range(idx+1,4):
        if cogs[i][6] != left:
            if t_dir == 1:
                t_dir = -1
            else :
                t_dir = 1
            selected_cog.append((i, t_dir))
            left = cogs[i][2]
        else:
            break

    for i in range(len(selected_cog)):
        n_idx, n_dir = selected_cog[i]
        if n_dir == 1:
            turnClockWise(cogs[n_idx])
        else:
            turnCounterClockWise(cogs[n_idx])

print(calc(cogs))