def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n, k = map(int, input().split()) #n k 입력

print(int(factorial(n) / (factorial(k) * factorial(n-k))))