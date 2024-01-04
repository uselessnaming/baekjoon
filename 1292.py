import sys

a, b = map(int, sys.stdin.readline().split())

i = [1, 0]
result = 0
idx = 1

while True:
    if a <= idx <= b:
        result += i[0]
    elif idx > b:
        break
    i[1] += 1
    if i[0] == i[1]:
        i[0] += 1
        i[1] = 0
    idx += 1

print(result)