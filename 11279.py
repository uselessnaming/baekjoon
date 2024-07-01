# 최대 힙
# 2024.07.01
# Silver2
import sys
from heapq import heappush, heappop
N = int(sys.stdin.readline())
heap = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heappop(heap))
    else:
        heappush(heap, -x)