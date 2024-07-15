# 보석 도둑
# 2024.07.15
# Gold 2
import sys
from heapq import heappush, heappop
answer = 0
N, K = map(int, sys.stdin.readline().split())
gems = [[*map(int,sys.stdin.readline().split())] for _ in range(N)]
bags = [int(input()) for _ in range(K)]
gems.sort()
bags.sort()
tmp = []

for bag in bags:
    while gems and gems[0][0] <= bag:
        heappush(tmp, -gems[0][1])
        heappop(gems)
    if tmp:
        answer -= heappop(tmp)
print(answer)