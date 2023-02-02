from collections import deque

input_data = deque(input())
data = deque()

for parentheses in input_data:
    if parentheses in "{[(":
        data.append(parentheses)
    elif parentheses in ")]}" and data:
        current = data.pop()
        if parentheses == ")" and current == "(":
            continue
        elif parentheses == "]" and current == "[":
            continue
        elif parentheses == "}" and current == "{":
            continue
        else:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
