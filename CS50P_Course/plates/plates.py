def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha():
        return False

    if not s[1].isalpha():
        return False

    if not s.isalnum():
        return False

    number_started = False
    for char in s:
        if char.isdigit():
            if char == '0' and not number_started:
                return False
            number_started = True
        elif number_started:
            return False

    return True


if __name__ == "__main__":
    main()
