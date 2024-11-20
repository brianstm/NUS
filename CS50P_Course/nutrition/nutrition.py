def main():
    calories = {
        "apple": 130,
        "avocado": 50,
        "sweet cherries": 100,
        "banana": 110,
        "blueberries": 80,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 60,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plum": 70,
        "raspberries": 60,
        "strawberries": 50,
        "watermelon": 80
    }
    fruit = input("Enter a fruit: ").strip().lower()

    if fruit in calories:
        print(f"Calories: {calories[fruit]}")
    else:
        return


if __name__ == "__main__":
    main()
