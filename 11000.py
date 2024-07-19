# 강의실 배정
# 2024.07.19
# Gold 5
import sys
from heapq import heappop, heappush
n = int(sys.stdin.readline())
study = []

for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    study.append((start, end))

study.sort(key = lambda x : x[0])
result = 1
heap = []
for start,end in study:
    if not heap:
        heappush(heap, end)
        continue
    if heap[0] <= start:
        heappop(heap)
    else:
        result += 1
    heappush(heap, end)
print(result)