word_list = []

max_length = 0

for _ in range(5):
    tmp = input()
    if len(tmp) > max_length:
        max_length = len(tmp)
    word_list.append(tmp)

result = ""

for i in range(max_length):
    for j in range(5):
        if i < len(word_list[j]):
            result += word_list[j][i]

print(result)