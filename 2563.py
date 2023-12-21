n = int(input()) #색종이 개수
locs = []

for _ in range(n):
    locs.append(map(int, input().split()))

total_map = [[0 for _ in range(100)] for _ in range(100)]

for loc in locs:
    x, y = loc

    for i in range(y-1,y+9):
        for j in range(x-1,x+9):
            total_map[i][j] = 1

s = 0
for rows in total_map:
    for r in rows:
        if r == 1:
            s += 1
print(s)