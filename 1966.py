from collections import deque

TC = int(input()) #Test Case Number

for _ in range(TC):
    n, m = map(int, input().split()) #문서 개수 / Queue에서의 위치
    weights = list(map(int, input().split())) # 가중치

    q = deque([])

    for i in range(len(weights)):
        q.append((weights[i],i))

    cnt = 0
    while q:

        while max(q)[0] != q[0][0]:
            weight, index = q.popleft()
            q.append((weight,index))

        target_weight, target_index = q.popleft()

        cnt += 1

        if target_index == m:
            break

    print(cnt)