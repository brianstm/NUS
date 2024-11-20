import csv
import sys

if len(sys.argv) != 3:
    sys.exit("Too few command-line arguments" if len(sys.argv)
             < 3 else "Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file) as file:
        reader = csv.DictReader(file)

        data = []
        for row in reader:
            last, first = row["name"].split(", ")
            data.append({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")

with open(output_file, "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in data:
        writer.writerow(row)
