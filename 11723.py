M = int(input())

sets = set()

for _ in range(M):
    command = input()

    if command == "all":
        sets = set(i for i in range(1,21))
    elif command == "empty":
        sets = set()
    else:
        command, n = command.split()
        n = int(n)

        if command == "add":
            sets.add(n)
        elif command == "remove":
            sets.discard(n)
        elif command == "check":
            if n in sets:
                print(1)
            else:
                print(0)
        elif command == "toggle":
            if n in sets:
                sets.remove(n)
            else:
                sets.add(n)