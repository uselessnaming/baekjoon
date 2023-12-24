import copy
import itertools

n, m = map(int, input().split())

city_map = []
for i in range(n):
    city_map.append(list(map(int, input().split())))

chicken_locs = []
house_locs = []

for i in range(n):
    for j in range(n):
        if city_map[i][j] == 1:
            house_locs.append((i,j))
        if city_map[i][j] == 2:
            chicken_locs.append((i,j))

result = 99999
combinations = itertools.combinations(chicken_locs, m)
for combination in combinations:
    tmp = 0
    for house_loc in house_locs:
        chi_len = 99999
        for j in range(m):
            chi_len = min(chi_len, abs(house_loc[0]-combination[j][0]) + abs(house_loc[1]-combination[j][1]))
        tmp += chi_len
    result = min(result, tmp)

print(result)