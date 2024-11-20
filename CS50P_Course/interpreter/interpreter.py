def interpreter():
    expression = input("Expression: ")

    x, y, z = expression.split()

    x = int(x)
    z = int(z)

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z

    print(f"{result:.1f}")


interpreter()
