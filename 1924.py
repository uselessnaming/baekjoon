#Year Month 입력
month, day = map(int, input().split())

day_list = [31,28,31,30,31,30,31,31,30,31,30,31]
date = ['SUN','MON','TUE','WED','THU','FRI','SAT']

s = 0

for i in range(1,month):
    s += day_list[i-1]

s += day

print(date[s % 7])