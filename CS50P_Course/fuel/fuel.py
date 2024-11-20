def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            display(percentage)
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = fraction.split('/')

    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    if x > y:
        raise ValueError("Numerator cannot be greater than the denominator.")

    percentage = (x / y) * 100
    return round(percentage)


def display(percentage):
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
    except ValueError:
        raise ValueError("Invalid input, non-integer values")

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if x > y:
        raise ValueError("Numerator cannot be greater than denominator")

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
