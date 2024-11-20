import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"
    match = re.match(pattern, ip)

    if match:
        return all(0 <= int(part) <= 255 for part in match.groups())
    return False


if __name__ == "__main__":
    main()
