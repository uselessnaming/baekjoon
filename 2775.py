TC = int(input()) #TestCase Number

under_floor = []
result = []

for _ in range(TC):
    k = int(input())
    n = int(input())

    floor = [j for j in range(1, n + 1)]

    for i in range(1,k+1):

        population = 0
        for j in range(n):
            population += floor[j]
            floor[j] = population

        under_floor = floor

    result.append(under_floor[n-1])

for r in result:
    print(r)