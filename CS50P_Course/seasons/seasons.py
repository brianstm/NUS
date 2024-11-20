from datetime import date
import inflect
import sys


def main():
    birthdate_str = input("Date of Birth (YYYY-MM-DD): ")
    print(convert(birthdate_str))


def convert(birthdate_str, today_date=None):
    try:
        birthday = date.fromisoformat(birthdate_str)
    except ValueError:
        sys.exit("Not a valid format.")

    today = today_date if today_date else date.today()
    minutes = (today - birthday).days * 24 * 60

    converter = inflect.engine()
    return converter.number_to_words(minutes, andword="").capitalize() + " minutes"


if __name__ == "__main__":
    main()
