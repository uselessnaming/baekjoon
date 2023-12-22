import copy
from collections import deque


def bfs(wall_first, wall_second, wall_third):
    tmp_lab = copy.deepcopy(lab)

    tmp_lab[wall_first[0]][wall_first[1]] = 1
    tmp_lab[wall_second[0]][wall_second[1]] = 1
    tmp_lab[wall_third[0]][wall_third[1]] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    q = deque(())

    for i in range(len(tmp_lab)):
        for j in range(len(tmp_lab[0])):
            if lab[i][j] == 2:
                q.append((i, j))

    while q:
        y, x = q.popleft()

        for _ in range(4):
            yy = y + dy[_]
            xx = x + dx[_]

            if 0 <= yy < n and 0 <= xx < m:
                if tmp_lab[yy][xx] == 0:
                    tmp_lab[yy][xx] = 2
                    q.append((yy, xx))

    s = 0

    for row in tmp_lab:
        for data in row:
            if data == 0:
                s += 1

    return s

n, m = map(int, input().split())

lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))

empty_loc = []

for col in range(len(lab)):
    for row in range(len(lab[0])):
        if lab[col][row] == 0:
            empty_loc.append((col,row))

result = 0

for i in range(len(empty_loc)-2):
    for j in range(i+1,len(empty_loc)-1):
        for k in range(j+1,len(empty_loc)):
            area = bfs(empty_loc[i],empty_loc[j],empty_loc[k])
            if area > result:
                result = area

print(result)