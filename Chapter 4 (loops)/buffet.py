# Create a tuple for a restaurant with a static menu.

buffet_foods = (
    'roast beef', 
    'mac and cheese', 
    'potatoes au gratin', 
    'fried chicken', 
    'green bean casserole'
    )

print("Our menu:")
for food in buffet_foods:
    print(food.capitalize())

# The menu did change, after all. Rewrite the tuple.

buffet_foods = (
    'sliced ham', 
    'mac and cheese', 
    'loaded potato skins', 
    'fried chicken', 
    'green been casserole'
    )

print("\nUpdated menu:")
for food in buffet_foods:
    print(food.capitalize())

# Note: .capitalize() caps the first letter of the string.