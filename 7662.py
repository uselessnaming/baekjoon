# 이중 우선순위 큐
# 2024.07.18
# Gold 4
from heapq import heappush, heappop
import sys
def isEmpty(nums):
    for item in nums:
        if item[1] > 0:
            return False
    return True

T = int(sys.stdin.readline())

for i in range(T):
    min_heap = []
    max_heap = []
    nums = dict()
    K = int(sys.stdin.readline())
    for j in range(K):
        op, value = sys.stdin.readline().split()
        value = int(value)
        if op == "I":
            if value in nums:
                nums[value] += 1
            else:
                heappush(min_heap, value)
                heappush(max_heap, -value)
                nums[value] = 1
        else:
            if not isEmpty(nums.items()):
                # 최솟값 삭제
                if value == -1:
                    while min_heap[0] not in nums or nums[min_heap[0]] < 1:
                        min_value = heappop(min_heap)
                        if min_value in nums:
                            del(nums[min_value])
                    nums[min_heap[0]] -= 1
                # 최댓값 삭제
                else:
                    while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
                        max_value = -heappop(max_heap)
                        if max_value in nums:
                            del(nums[max_value])
                    nums[-max_heap[0]] -= 1
    if isEmpty(nums.items()):
        print("EMPTY")
    else:
        while min_heap[0] not in nums or nums[min_heap[0]] < 1:
            heappop(min_heap)
        while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
            heappop(max_heap)
        print(-max_heap[0], min_heap[0])