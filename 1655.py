# 가운데를 말해요
# 2024.07.01
# Gold 2
import sys
from heapq import heappop, heappush
N = int(sys.stdin.readline())
leftHeap = []
rightHeap = []
for i in range(N):
    x = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap):
        heappush(leftHeap, -x)
    else:
        heappush(rightHeap, x)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heappop(leftHeap)
        rightValue = heappop(rightHeap)

        heappush(leftHeap, -rightValue)
        heappush(rightHeap, -leftValue)

    print(-leftHeap[0])