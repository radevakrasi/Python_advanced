def rectangle(length, width):
    if isinstance(length, int) and isinstance(width, int):

        def area():
            return length * width

        def perimeter():
            return 2 * (length + width)

        return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

    return "Enter valid values!"

print(rectangle(2, 10))
print(rectangle('2', 10))
