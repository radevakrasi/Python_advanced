nums = input().split()
reverse = []

for i in range(len(nums)):
    reverse.append(nums.pop())

print(" ".join(reverse))