import math

N = input()

num_list = [0 for i in range(9)]

for ch in N:
    if int(ch) == 9:
        num_list[6] += 1
    else:
        num_list[int(ch)] += 1

num_list[6] = math.ceil(num_list[6]/2)

print(max(num_list))