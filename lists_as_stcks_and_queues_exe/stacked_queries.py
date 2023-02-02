n = int(input())
collect = []

for i in range(n):
    command = input()
    number = command.split()

    if int(number[0]) == 1:
        add = int(number[1])
        collect.append(add)
    elif int(command) == 2:
        if collect:
            collect.pop()
    elif int(command) == 3:
        if collect:
            print(max(collect))

    elif int(command) == 4:
        if collect:
            print(min(collect))

collect.reverse()
print(*collect, sep=", ")
