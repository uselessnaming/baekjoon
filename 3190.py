import sys
from collections import deque

#보드 크기
n = int(sys.stdin.readline())

board = [[0 for i in range(n+1)] for j in range(n+1)]

#사과의 개수
k = int(sys.stdin.readline())

for i in range(k):
    y, x = map(int, sys.stdin.readline().split())
    board[y][x] = 1

board[1][1] = -1

#뱀의 방향 변환 횟수
l = int(sys.stdin.readline())

head_y, head_x = 1,1
tail_y, tail_x = 1,1

#우, 하, 좌, 상
dx = [1,0,-1,0]
dy = [0,1,0,-1]

#방향
way = 0

#결과
cnt = 0

c_list = deque([])

before = 0

for i in range(l+1):
    if i != l :
        x, c = sys.stdin.readline().split()
        x = int(x)

        for _ in range(before, x):

            cnt += 1

            head_x += dx[way]
            head_y += dy[way]

            c_list.append(way)

            if 0 < head_x < n + 1 and 0 < head_y < n + 1 and board[head_y][head_x] != -1:
                # 사과 체크
                if board[head_y][head_x] != 1:
                    board[tail_y][tail_x] = 0
                    tail_way = c_list.popleft()
                    tail_y += dy[tail_way]
                    tail_x += dx[tail_way]
                    board[tail_y][tail_x] = -1
                board[head_y][head_x] = -1
            else:
                print(cnt)
                exit(0)

        if c == "L":
            way = (way + 3) % 4
        elif c == "D":
            way = (way + 1) % 4

        before = x
    else :
        while True:

            cnt += 1

            head_x += dx[way]
            head_y += dy[way]

            c_list.append(way)

            if 0 < head_x < n + 1 and 0 < head_y < n + 1 and board[head_y][head_x] != -1:
                # 사과 체크
                if board[head_y][head_x] != 1:
                    board[tail_y][tail_x] = 0
                    tail_way = c_list.popleft()
                    tail_y += dy[tail_way]
                    tail_x += dx[tail_way]
                    board[tail_y][tail_x] = -1
                board[head_y][head_x] = -1
            else:
                print(cnt)
                exit(0)