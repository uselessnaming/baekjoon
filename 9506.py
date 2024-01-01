import sys

while True:
    n = int(sys.stdin.readline())

    if n == -1:
        break

    result = []

    for i in range(1,n//2+1):
        if n % i == 0:
            result.append(i)

    print(n, end = " ")
    if n == sum(result):
        print("=", end = " ")
        for r in result:
            print(r, end = " ")
            if r != result[-1]:
                print("+", end = " ")
        print()
    else:
        print("is NOT perfect.")