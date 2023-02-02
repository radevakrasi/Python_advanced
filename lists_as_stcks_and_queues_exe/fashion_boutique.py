cloths_list = [int(x) for x in input().split()]
capacity = int(input())
current_capacity = capacity
racks = 1

while cloths_list:
    cloths = cloths_list.pop()
    if current_capacity >= cloths:
        current_capacity -= cloths

    else:
        cloths_list.append(cloths)
        racks += 1
        current_capacity = capacity

print(racks)

