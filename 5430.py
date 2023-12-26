from collections import deque
import sys

tc = int(input())

for _ in range(tc):
    commands = input().rstrip()
    n = int(input())

    q = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    front = True

    flag = 0

    if n == 0:
        q = []
    for command in commands:
        if command == "R":
            front = not front
        elif command == "D":
            if q:
                if front:
                    q.popleft()
                else:
                    q.pop()
            else:
                flag = 1
                print("error")
                break
    if flag == 0:
        if front:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")