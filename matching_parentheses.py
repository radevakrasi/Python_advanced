text = input()
start = []

for i in range (len(text)):
    if text[i] == "(":
        start.append(i)
    elif text[i] == ")":
        start_index = start.pop()
        result = text[start_index:i+1]
        print(result)