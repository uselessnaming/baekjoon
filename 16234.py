import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())

space = []

for _ in range(n):
    space.append(list(map(int, sys.stdin.readline().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(start_y,start_x,cnt):


    q = deque([(start_y,start_x)])
    visited[start_y][start_x] = cnt

    while q:
        y, x = q.popleft()

        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]

            if 0<=yy<n and 0<=xx<n and not visited[yy][xx]:
                if l <= abs(space[y][x] - space[yy][xx]) <= r:
                    visited[yy][xx] = cnt
                    q.append((yy, xx))


result = 1

while True:
    cnt = 1
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, cnt)
                cnt += 1

    if cnt-1 == n*n:
        break

    values = [0 for _ in range(cnt-1)]
    nums = [0 for _ in range(cnt-1)]

    tmp = 0
    for i in range(n):
        for j in range(n):
            idx = visited[i][j] - 1
            nums[idx] += 1
            values[idx] += space[i][j]

    for i in range(n):
        for j in range(n):
            space[i][j] = values[visited[i][j]-1] // nums[visited[i][j]-1]

    result += 1

print(result-1)