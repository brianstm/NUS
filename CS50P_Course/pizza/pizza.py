import sys
import os
import csv
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments" if len(sys.argv)
             < 2 else "Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

if not os.path.exists(filename):
    sys.exit("File does not exist")


def display_csv_as_table(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        table = [row for row in reader]
        print(tabulate(table[1:], headers=table[0], tablefmt="grid"))


if __name__ == "__main__":
    display_csv_as_table(filename)
