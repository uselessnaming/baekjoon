# 카드 정렬하기
# 2024.07.01
# Gold 4
import sys
from heapq import heappush, heappop
N = int(sys.stdin.readline())
heap = []
for i in range(N):
    x = int(sys.stdin.readline())
    heappush(heap, x)
cnt = 0
while len(heap) >= 2:
    tmp = heappop(heap) + heappop(heap)
    cnt += tmp
    heappush(heap, tmp)
print(cnt)