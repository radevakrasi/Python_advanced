# def recursive_power(number, power):
#     if power == 0:
#         return 1
#     return number * recursive_power(number, power - 1)
def recursive_power(number, power):
    return number ** power

print(recursive_power(2, 10))
print(recursive_power(10, 100))
