import copy
import itertools
from collections import deque

def calDist(combinations, house_locs):
    tmp_map = copy.deepcopy(city_map)

    for combination in combinations:
        y, x = combination
        tmp_map[y][x] = 2

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    q = deque([])

    for house_loc in house_locs:
        q.append((house_loc,0))

    s = 0

    while q:
        loc, cnt = q.popleft()
        y, x = loc

        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]

            if 0<=xx<len(tmp_map) and 0<=yy<len(tmp_map):
                if tmp_map[yy][xx] == 0:
                    q.append(((yy,xx),cnt+1))
                    tmp_map[yy][xx] = -1
                if tmp_map[yy][xx] == 1:
                    q.append(((yy,xx),cnt+1))
                    tmp_map[yy][xx] = -1
                if tmp_map[yy][xx] == 2:
                    s += cnt+1
                    print(yy, xx, s)
                    print(tmp_map)
    return s

n, m = map(int, input().split())

city_map = []
for i in range(n):
    city_map.append(list(map(int, input().split())))

chicken_locs = []
house_locs = []

for i in range(n):
    for j in range(n):
        if city_map[i][j] == 1:
            house_locs.append((i,j))
        if city_map[i][j] == 2:
            chicken_locs.append((i,j))
            city_map[i][j] = 0

result = 99999999
for i in range(1, m+1):
    com = list(itertools.combinations(chicken_locs, i))
    print(com)
    for c in com:
        tmp = calDist(c, house_locs)
        if tmp < result:
            result = tmp

print(result)