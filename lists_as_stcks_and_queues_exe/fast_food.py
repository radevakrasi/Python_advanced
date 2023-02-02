from collections import deque

all_food = int(input())
orders = deque(int(x) for x in input().split(" "))

print(max(orders))

while orders:
    order = orders.popleft()
    if all_food - order >= 0:
        all_food -= order
        continue
    else:
        orders.appendleft(order)
        print(f"Orders left: {' '.join([str(x) for x in orders])}")
        break
else:
    print("Orders complete")
