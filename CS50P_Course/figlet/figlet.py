import sys
import pyfiglet
import random


def main():
    fonts = pyfiglet.FigletFont.getFonts()

    if len(sys.argv) == 1:
        selected_font = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
        if sys.argv[2] in fonts:
            selected_font = sys.argv[2]
        else:
            sys.exit("Invalid usage: Font not found")
    else:
        sys.exit("Invalid")

    figlet = pyfiglet.Figlet(font=selected_font)

    text = input("Input: ")

    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
