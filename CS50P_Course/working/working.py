import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.match(
        r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$", s)
    if not match:
        raise ValueError("Invalid time format")

    start_hour, start_minute, start_period = match.group(
        1), match.group(2), match.group(3)
    end_hour, end_minute, end_period = match.group(
        4), match.group(5), match.group(6)

    start_minute = start_minute if start_minute else "00"
    end_minute = end_minute if end_minute else "00"

    start_24 = convert_to_24_hour(start_hour, start_minute, start_period)
    end_24 = convert_to_24_hour(end_hour, end_minute, end_period)

    return f"{start_24} to {end_24}"


def convert_to_24_hour(hour, minute, period):
    hour = int(hour)
    minute = int(minute)

    if hour < 1 or hour > 12 or minute < 0 or minute >= 60:
        raise ValueError("Invalid time value")

    if period == "AM":
        hour = 0 if hour == 12 else hour
    else:
        hour = 12 if hour == 12 else hour + 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
