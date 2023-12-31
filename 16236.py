import sys
from collections import deque

def bfs(y, x):

    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[y][x] = 1

    locs = []

    q = deque([(y,x)])

    while q:

        y, x, = q.popleft()

        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]

            if 0 <= yy < n and 0 <= xx < n and space[yy][xx] <= size[0] and visited[yy][xx] == 0:
                visited[yy][xx] = visited[y][x] + 1
                # 물고기를 먹었을 때
                if 0 < space[yy][xx] < size[0]:
                    locs.append((visited[yy][xx]-1,yy,xx))
                q.append((yy, xx))

    return sorted(locs, key = lambda x : (x[0], x[1], x[2]))

n = int(sys.stdin.readline())

space = [] #지도 전체 공간

for _ in range(n):
    space.append(list(map(int, sys.stdin.readline().split())))

y,x = 0, 0
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            y, x = i, j
            space[i][j] = 0

#움직임의 순서는 상, 좌, 하, 우
dy = [-1,0,1,0]
dx = [0,-1,0,1]

cnt = 0
size = [2,0]

while True:
    result = bfs(y,x)

    if not result:
        break
    step, y, x = result[0]
    space[y][x] = 0
    cnt += step

    size[1] += 1
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

print(cnt)