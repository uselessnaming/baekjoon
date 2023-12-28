import sys

n, m = map(int, sys.stdin.readline().split())

num_map = []
for _ in range(n):
    num_map.append(list(map(int, sys.stdin.readline().split())))

result = []

for i in range(n):
    for j in range(m):
        #세로
        if i+3 < len(num_map):
            tmp = 0
            for k in range(i,i+4):
                tmp += num_map[k][j]
            result.append(tmp)
        #가로
        if j+3 < len(num_map[0]):
            tmp = 0
            for k in range(j,j+4):
                tmp += num_map[i][k]
            result.append(tmp)
        #네모
        if i+1 < len(num_map) and j+1 < len(num_map[0]):
            tmp = num_map[i][j] + num_map[i+1][j] + num_map[i][j+1] + num_map[i+1][j+1]
            result.append(tmp)
        #ㅗ모양
        if j+2 < len(num_map[0]):
            std_num = num_map[i][j] + num_map[i][j+1] + num_map[i][j+2]
            if i-1 > -1:
                result.append(std_num + num_map[i - 1][j + 1])
            if i+1 < len(num_map):
                result.append(std_num + num_map[i + 1][j + 1])
        if i+2 < len(num_map):
            std_num = num_map[i][j] + num_map[i+1][j] + num_map[i+2][j]
            if j-1 > -1:
                result.append(std_num + num_map[i+1][j-1])
            if j+1 < len(num_map[0]):
                result.append(std_num + num_map[i+1][j+1])
        #L모양
        if i+2 < len(num_map):
            std_num = num_map[i][j] + num_map[i+1][j] + num_map[i+2][j]
            if j-1 > -1:
                result.append(std_num + num_map[i+2][j-1])
            if j+1 < len(num_map[0]):
                result.append(std_num + num_map[i+2][j+1])
            std_num = num_map[i][j]
            if j-1 > -1:
                result.append(std_num + num_map[i][j-1] + num_map[i+1][j-1] + num_map[i+2][j-1])
            if j+1 < len(num_map[0]):
                result.append(std_num + num_map[i][j+1] + num_map[i+1][j+1] + num_map[i+2][j+1])
        if j+2 < len(num_map[0]):
            std_num = num_map[i][j] + num_map[i][j+1] + num_map[i][j+2]
            if i-1 > -1:
                result.append(std_num + num_map[i-1][j+2])
            if i+1 < len(num_map):
                result.append(std_num + num_map[i+1][j+2])
            std_num = num_map[i][j]
            if i-1 > -1:
                result.append(std_num + num_map[i-1][j] + num_map[i-1][j+1] + num_map[i-1][j+2])
            if i+1 < len(num_map):
                result.append(std_num + num_map[i+1][j] + num_map[i+1][j+1] + num_map[i+1][j+2])
        #z모양
        if j+2 < len(num_map[0]):
            std_num = num_map[i][j] + num_map[i][j+1]
            if i-1 > -1:
                result.append(std_num + num_map[i-1][j+1] + num_map[i-1][j+2])
            if i+1 < len(num_map):
                result.append(std_num + num_map[i+1][j+1] + num_map[i+1][j+2])
        if i+2 < len(num_map):
            std_num = num_map[i][j] + num_map[i+1][j]
            if j-1 > -1:
                result.append(std_num + num_map[i+1][j-1] + num_map[i+2][j-1])
            if j+1 < len(num_map[0]):
                result.append(std_num + num_map[i+1][j+1] + num_map[i+2][j+1])
print(max(result))