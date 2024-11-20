import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Failed to fetch Bitcoin price data")

    data = response.json()
    try:
        bitcoin_price_usd = data["bpi"]["USD"]["rate_float"]
    except KeyError:
        sys.exit("Error parsing data")

    total_cost = num_bitcoins * bitcoin_price_usd

    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()
