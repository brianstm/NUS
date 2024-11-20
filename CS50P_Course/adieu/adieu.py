def main():
    names = []
    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        pass

    farewell_message = format_farewell(names)
    print(farewell_message)


def format_farewell(names):
    if len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        return f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}"


if __name__ == "__main__":
    main()
