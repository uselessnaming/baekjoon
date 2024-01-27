import sys

N = int(sys.stdin.readline())

for _ in range(N):
    sentence = list(sys.stdin.readline().strip().split())

    result = ""
    n_s = len(sentence)
    for i in range(len(sentence)):
        n_w = len(sentence[i])
        for j in range(n_w-1,-1,-1):
            result += sentence[i][j]
        if i != n_s - 1:
            result += " "
    print(result)