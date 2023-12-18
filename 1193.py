n = int(input()) #입력

# 1, 2, 3, 4 로 각 열의 크기 i가 증가 >> 분수의 값은 i + j / len(i) - j
j = 1

while True:
    n -= j

    if n <= 0:
        break

    j += 1

result = ''
if j % 2 == 0:
    result = str(j+n) + '/' + str(abs(n)+1)
else:
    result = str(abs(n)+1) + '/' + str(j+n)
print(result)