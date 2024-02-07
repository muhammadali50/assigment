#seperate
budget = int(input("Enter your budget: "))  # Get user input for budget

shopping_list = {}  # Initialize an empty dictionary for the shopping list

while True:
    item_name = input("Enter item name (or 'done' to finish): ")
    if item_name == "done":
        break
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))

    shopping_list[item_name] = {"quantity": quantity, "price": price}

# ... (rest of the code for calculating total cost and checking budget)
