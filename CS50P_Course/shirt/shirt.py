import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    sys.exit("Too few command-line arguments" if len(sys.argv)
             < 3 else "Too many command-line arguments")

valid_extensions = (".jpg", ".jpeg", ".png")
input_file = sys.argv[1]
output_file = sys.argv[2]

if not (input_file.lower().endswith(valid_extensions) and output_file.lower().endswith(valid_extensions)):
    sys.exit("Invalid output")

if os.path.splitext(input_file)[1].lower() != os.path.splitext(output_file)[1].lower():
    sys.exit("Input and output have different extensions")

if not os.path.isfile(input_file):
    sys.exit("Input does not exist")

try:
    with Image.open(input_file) as img, Image.open("shirt.png") as shirt:
        img = ImageOps.fit(img, shirt.size)
        img.paste(shirt, (0, 0), shirt)
        img.save(output_file)
except Exception as e:
    sys.exit(f"An error occurred: {e}")
