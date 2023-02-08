def sorting_cheeses(**kwargs):
    sorted_cheese = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ''
    for name, quantity in sorted_cheese:
        result += name + "\n"
        sorted_quantity = sorted(quantity,reverse=True)
        result += "\n".join(str(x) for x in sorted_quantity) + "\n"

    return result



print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
