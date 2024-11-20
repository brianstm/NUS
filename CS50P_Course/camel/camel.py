def main():
    camel_case = input("camelCase: ").strip()

    snake_case = convert(camel_case)

    print(snake_case)


def convert(camel_case):
    snake_case = []

    for char in camel_case:
        if char.isupper():
            snake_case.append('_')
            snake_case.append(char.lower())
        else:
            snake_case.append(char)

    return ''.join(snake_case)


if __name__ == "__main__":
    main()
