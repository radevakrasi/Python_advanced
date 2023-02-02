operations = int(input())
parking = set()
for i in range(operations):
    command, number = input().split(", ")
    if command == "IN":
        parking.add(number)
    elif command == "OUT":
        parking.remove(number)

if parking:
    for i in parking:
        print(i)
else:
    print("Parking Lot is Empty")
