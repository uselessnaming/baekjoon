import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

space = []

for i in range(n):
    space.append(list(sys.stdin.readline().strip()))

r_x, r_y, b_x, b_y = 0, 0, 0, 0

for i in range(n):
    for j in range(m):
        if space[i][j] == 'R':
            r_y, r_x = i, j
        elif space[i][j] == 'B':
            b_y, b_x = i, j

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(r_y, r_x, b_y, b_x):
    q = deque()
    q.append((r_y, r_x, b_y, b_x))
    visited = []
    visited.append((r_y, r_x, b_y, b_x))
    count = 0
    while q:
        for _ in range(len(q)):
            r_y, r_x, b_y, b_x = q.popleft()
            if count > 10:
                print(-1)
                return
            if space[r_y][r_x] == 'O':
                print(count)
                return
            for i in range(4):
                rr_y, rr_x = r_y, r_x
                while True:
                    rr_y += dy[i]
                    rr_x += dx[i]

                    if space[rr_y][rr_x] == '#':
                        rr_y -= dy[i]
                        rr_x -= dx[i]
                        break
                    if space[rr_y][rr_x] == 'O':
                        break

                bb_y, bb_x = b_y, b_x
                while True:
                    bb_y += dy[i]
                    bb_x += dx[i]

                    if space[bb_y][bb_x] == '#':
                        bb_y -= dy[i]
                        bb_x -= dx[i]
                        break
                    if space[bb_y][bb_x] == 'O':
                        break

                if space[bb_y][bb_x] == 'O':
                    continue
                if rr_y == bb_y and rr_x == bb_x:
                    if abs(rr_y - r_y) + abs(rr_x - r_x) > abs(bb_x - b_x) + abs(bb_y - b_y):
                        rr_y -= dy[i]
                        rr_x -= dx[i]
                    else :
                        bb_y -= dy[i]
                        bb_x -= dx[i]
                if (rr_y, rr_x, bb_y, bb_x) not in visited:
                    q.append((rr_y, rr_x, bb_y, bb_x))
                    visited.append((rr_y, rr_x, bb_y, bb_x))
        count += 1
    print(-1)

bfs(r_y, r_x, b_y, b_x)