n, m = map(int,input().split())

start_y, start_x, way = map(int, input().split()) #현재 위치, 보는 방향

if way == 1:
    way = 3
elif way == 3:
    way = 1

locs = []
for i in range(n):
    locs.append(list(map(int, input().split())))
visited = [[False for _ in range(m)] for _ in range(n)]
visited[start_y][start_x] = True

dx = [0,-1,0,1]
dy = [-1,0,1,0]

cnt = 1

x, y, way_tmp = start_x, start_y, way
isClean = False
while True:
    isClean = False
    for _ in range(1,5):
        way_tmp = (way + _) % 4

        xx = x + dx[way_tmp]
        yy = y + dy[way_tmp]

        if 0<=xx<m and 0<=yy<n:
            if not visited[yy][xx] and locs[yy][xx] == 0:
                cnt += 1
                visited[yy][xx] = True
                x = xx
                y = yy
                isClean = True
                way = way_tmp
                break

    if not isClean:
        way_tmp = way + 2
        if way_tmp >= 4:
            way_tmp -= 4
        xx = x + dx[way_tmp]
        yy = y + dy[way_tmp]
        if locs[yy][xx] == 1:
            break
        y = yy
        x = xx

print(cnt)

tmp_cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            tmp_cnt += 1
print(tmp_cnt)