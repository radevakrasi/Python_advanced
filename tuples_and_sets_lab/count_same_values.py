numbers = input().split()

counts = {}
for n in numbers:
    if n not in counts.keys():
        counts[n] = 0
    counts[n] += 1

for key, value in counts.items():
    f_key = float(key)

    print(f"{f_key:.1f} - {value} times")
