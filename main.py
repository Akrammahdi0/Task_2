
import random
import math

categories = {
    "Pizza": ["Margherita", "Pepperoni", "Hawaiian", "Veggie", "BBQ Chicken",
              "Four Cheese"],
    "Burgers": ["Beef", "Chicken", "Veggie"],
    "Pasta": ["Spaghetti Bolognese", "Carbonara"],
    "Salad": [],
    "Sushi": ["California Roll", "Tuna Nigiri", "Salmon Sashimi",
              "Dragon Roll", "Avocado Roll"],
    "Dessert": ["Cheesecake"]
}

category_map = {
    1: "Burgers",
    2: "Pasta",
    3: "Pizza",
    4: "Sushi",
    5: "Salad",
    6: "Dessert"
}


def get_user_preferences():
    print("Available Categories:")
    for num, name in category_map.items():
        print(f"{num}: {name}")

    input_str = input(
        "Enter the numbers of the categories you're interested in "
        "(comma-separated): "
    )

    try:
        selected_numbers = [int(x.strip()) for x in input_str.split(",")]
        selected_categories = [category_map[num] for num in selected_numbers
                               if num in category_map]
        if not selected_categories:
            print("No valid categories selected.")
            return []
        return selected_categories
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return []


def main():
    user_preferences = get_user_preferences()
    print("User preferences:", user_preferences)

    print("\nSelected Categories and Available Items:")
    for category in user_preferences:
        items = categories.get(category, [])
        if items:
            print(f"  {category}: {items}")
        else:
            print(f"  {category}: No available items")

    if not user_preferences:
        print("No preferences selected. Exiting.")
    else:
        dice_roll = random.randint(1, 6)
        print(f"Dice roll: {dice_roll}")

        filtered_items = {
            category: items for category, items in categories.items()
            if category in user_preferences and items
        }

        if not filtered_items:
            print("No items available in selected categories.")
        else:
            total_preferences = len(filtered_items)
            ratio = math.ceil(dice_roll / total_preferences)
            print(f"Initial items per category (rounded up): {ratio}")
            recommended_items = []
            remaining_slots = dice_roll

            for category, items in filtered_items.items():
                if remaining_slots == 0:
                    break
                count = min(ratio, len(items), remaining_slots)
                chosen = random.sample(items, count)
                print(f"From {category}, selected: {chosen}")
                recommended_items.extend(chosen)
                remaining_slots -= count

            if len(recommended_items) < dice_roll:
                remaining = dice_roll - len(recommended_items)
                print(f"Need {remaining} more items. Trying to fill from all"
                      "remaining items.")

                all_available = [
                    item for cat_items in categories.values()
                    for item in cat_items if item not in recommended_items
                ]
                extra = random.sample(
                    all_available, min(remaining, len(all_available)))
                recommended_items.extend(extra)

            print("\nFinal Recommendations:")
            print(recommended_items)


main()
