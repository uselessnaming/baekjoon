import sys
from collections import deque

def turn(command):

    if command == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[0], dice[5], dice[1], dice[2], dice[4], dice[3]
    elif command == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[0], dice[2], dice[3], dice[5], dice[4], dice[1]
    elif command == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[4], dice[3], dice[5], dice[0]
    elif command == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[5], dice[1], dice[0], dice[3], dice[2], dice[4]


n, m, y, x, k = map(int, sys.stdin.readline().split())

space = []

for _ in range(n):
    space.append(list(map(int, sys.stdin.readline().split())))

q = deque(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

dice = [0 for i in range(6)]

while q:
    command = q.popleft()

    xx, yy = x+dx[command-1], y+dy[command-1]

    if 0<=yy<n and 0<=xx<m:
        turn(command)

        y, x = yy, xx

        if space[yy][xx] == 0:
            space[yy][xx] = dice[-1]
        else:
            dice[-1] = space[yy][xx]
            space[yy][xx] = 0

        print(dice[2])