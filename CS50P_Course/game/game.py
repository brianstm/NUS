import random


def main():
    level = get_positive_integer("Level: ")

    number = random.randint(1, level)

    while True:
        guess = get_positive_integer("Guess: ")

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass


if __name__ == "__main__":
    main()
