def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            else:
                month_name, day_year = date.split(" ", 1)
                if "," in day_year:
                    day, year = day_year.split(", ")
                    month = months.index(month_name) + 1
                    day = int(day)
                    year = int(year)
                else:
                    raise ValueError("Invalid date format")

            if month < 1 or month > 12 or day < 1 or day > 31:
                raise ValueError("Invalid date values")

            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

        except (ValueError, IndexError):
            pass


if __name__ == "__main__":
    main()
