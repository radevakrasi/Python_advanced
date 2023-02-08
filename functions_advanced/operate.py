def operate(operator, *args):
    if operator == "+":
        return sum(args)
    elif operator == "-":
        result = args[0]
        for i in range(len(args) - 1):
            result -= args[i + 1]
        return result
    elif operator == "*":
        result = args[0]
        for i in range(len(args) - 1):
            result *= args[i + 1]
        return result
    elif operator == "/":
        if 0 in args:
            return "Invalid operation"
        result = args[0]
        for i in range(len(args) - 1):
            result /= args[i + 1]
        return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
