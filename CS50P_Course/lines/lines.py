import sys
import os

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments" if len(sys.argv)
             < 2 else "Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Not a Python file")

if not os.path.exists(filename):
    sys.exit("File does not exist")


def count_lines_of_code(filename):
    with open(filename, "r") as file:
        count = 0
        for line in file:
            stripped_line = line.strip()
            if stripped_line and not stripped_line.startswith("#"):
                count += 1
        return count


if __name__ == "__main__":
    print(count_lines_of_code(filename))
