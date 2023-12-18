n = int(input()) #입력

# 1, 2, 3, 4 로 각 열의 크기 i가 증가 >> 분수의 값은 i + j / len(i) - j
j = 1

while True:
    n -= j

    if n <= 0:
        break

    j += 1

tmp = [i for i in range(1,j+1)]
middle = j // 2

result = ''
if j % 2 == 0:
    result = str(tmp[j+n-1]) + '/' + str(tmp[abs(n)])
else:
    result = str(tmp[abs(n)]) + '/' + str(tmp[j+n-1])
print(result)