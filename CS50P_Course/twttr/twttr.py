def main():
    text = input("Input: ")

    vowels = "aeiouAEIOU"

    no_vowels = ''.join([char for char in text if char not in vowels])

    print(f"Output: {no_vowels}")


def shorten(word):
    vowels = "aeiouAEIOU"
    return "".join([char for char in word if char not in vowels])


if __name__ == "__main__":
    main()
