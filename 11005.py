import sys

n, b = map(int, sys.stdin.readline().split())

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
result = ""

r = n

while n // b > 0:
    r = n % b
    n = n // b

    if r < 10:
        result += str(r)
    else:
        result = result + alpha[r - 10]

if n < 10:
    result += str(n)
else:
    result += alpha[n - 10]

answer = ""
for ch in range(len(result),0,-1):
    answer += result[ch-1]

print(answer)