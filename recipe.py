ingredients_and_amounts = {
    "flour": 2,
    "sugar": 3,
    "milk": 4,
    "cream": 1,
    "coco powder": 2,
}
original_servings = 6
num_servings = int(input("How many servings do you want? "))
change_factor = num_servings / original_servings
print("Here's the recipe for", num_servings, "servings:")
new_flour_amount = ingredients_and_amounts["flour"] * change_factor
new_sugar_amount = ingredients_and_amounts["sugar"] * change_factor
new_milk_amount = ingredients_and_amounts["milk"] * change_factor
new_cream_amount = ingredients_and_amounts["cream"] * change_factor
new_coco_powder_amount = ingredients_and_amounts["coco powder"] * change_factor
print(f"Flour: {new_flour_amount:.2f} cups")
print(f"Sugar: {new_sugar_amount:.2f} cups")
print(f"Milk: {new_milk_amount:.2f} cups")
print(f"Cream: {new_cream_amount:.2f} cups")
print(f"Coco powder: {new_coco_powder_amount:.2f} cups")