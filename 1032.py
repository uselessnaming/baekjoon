import sys

n = int(sys.stdin.readline())

result = ""

for i in range(n):
    file_name = sys.stdin.readline()
    if result == "":
        result = file_name
    else:
        for ch in range(len(file_name)):
            if result[ch] != file_name[ch]:
                result = result[:ch] + "?" + result[ch+1:]
print(result)