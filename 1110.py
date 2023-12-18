n = int(input())

cnt = 0 #반복 횟수
nextN = n

while True:
    nextN = ((nextN % 10) * 10) + (((nextN // 10) + (nextN % 10)) % 10)
    cnt += 1

    if nextN == n:
        break

print(cnt)