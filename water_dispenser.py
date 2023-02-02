from collections import deque

water = int(input())
line = deque()
command = input()
while command != "Start":
    if command.isalpha():
        line.append(command)
    command = input()

while True:
    command = input()
    if command == "End":
        break

    if command.isdigit():
        if water >= int(command):
            print(f"{line.popleft()} got water")
            water -= int(command)
        else:
            print(f"{line.popleft()} must wait")
    else:
        liters = command.split()
        lit = liters[1]
        water += int(lit)

print(f"{water} liters left")
