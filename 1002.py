import sys
import math

tc = int(sys.stdin.readline())

for _ in range(tc):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    if dist == 0 and r1 == r2:
        print(-1)
    elif abs(r1-r2) == dist or r1 + r2 == dist:
        print(1)
    elif abs(r1-r2) < dist < (r1+r2):
        print(2)
    else:
        print(0)