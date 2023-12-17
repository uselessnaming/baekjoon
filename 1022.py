# 입력 받음
# 중앙을 기준으로 홀수는 우측, 아래 / 짝수는 좌측, 위
r1, c1, r2, c2 = input().split()
r1 = int(r1)
c1 = int(c1)
r2 = int(r2)
c2 = int(c2)

# 가장 큰 수를 기준으로 정사각형 표를 만들고 부분을 떼어와서 출력
maxNum = max(abs(r1), abs(r2), abs(c1), abs(c2))
n = maxNum*2 +1

result = [['0' for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]

#맵 세팅
i = n-1
j = n-1
cnt = n*n
roundCnt = 0
_ = 0
maxLength = 0

start_x = n//2 + c1
start_y = n//2 + r1
end_x = n//2 + c2
end_y = n//2 + r2

while True:

    if start_x <= j <= end_x and start_y <= i <= end_y:
        if len(str(cnt)) > maxLength:
            maxLength = len(str(cnt))
        result[i-start_y][j-start_x] = cnt


    cnt -= 1

    if cnt == 0:
        break

    if i == n-1-roundCnt:
        if j == 0+roundCnt:
            i -= 1
        else:
            j -= 1
    elif j == 0+roundCnt:
        if i == 0+roundCnt:
            j += 1
        else:
            i -= 1
    elif i == 0+roundCnt:
        if j == n-1-roundCnt:
            i += 1
        else:
            j += 1
    elif j == n-1-roundCnt:
        if _ == 2*(maxNum - roundCnt - 1):
            j -= 1
            roundCnt += 1
            _ = 0
        else:
            i += 1
            _ += 1

for i in range(len(result)):
    for j in range(len(result[0])):
        tmp = str(result[i][j])
        if j != len(result[0])-1:
            if len(tmp) != maxLength:
                tmp = ' ' * (maxLength - len(tmp)) + tmp
            print(tmp, end = ' ')
        else:
            if len(tmp) != maxLength:
                tmp = ' ' * (maxLength - len(tmp)) + tmp
            print(tmp)