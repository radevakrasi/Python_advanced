text = list(input())
stack_list = []
for i in range(len(text)):
    stack_list.append(text.pop())

print("".join(stack_list))
 