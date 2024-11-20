def main():
    amount_due = 50
    while amount_due > 0:
        coin = int(input("Insert Coin: "))

        if coin in [25, 10, 5]:
            amount_due -= coin
            if amount_due > 0:
                print(f"Amount Due: {amount_due}")

        else:
            print(f"Amount Due: {amount_due}")

    change_owed = abs(amount_due)
    print(f"Change Owed: {change_owed}")


if __name__ == "__main__":
    main()
