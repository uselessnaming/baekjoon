n = int(input()) #입력 횟수

info = []
result = []

for _ in range(n):
    weight, height = map(int, input().split())
    info.append((weight, height))

for i in range(len(info)):
    weight, height = info[i][0], info[i][1]

    cnt = 0 #나보다 덩치가 큰 사람의 수

    for j in range(len(info)):
        if i != j:
            if weight < info[j][0] and height < info[j][1]:
                cnt += 1

    result.append(cnt+1)

for r in result:
    print(r, end = ' ')