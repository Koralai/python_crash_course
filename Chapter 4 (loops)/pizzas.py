# Create a list of pizzas.

pizzas = ['margherita', 'veggie', 'Hawaiian', 'thin crust', 'deep dish']

# Loop through the list, printing a statement about each type of pizza.

for pizza in pizzas:
    print(f"I would love a slice of {pizza} pizza right now.")

# Print a final statement after the loop has finished.

print("I'm making myself hungry...")

# Print info on "slices" of this list (haha).

print(f"The first three items in the list are: {pizzas[:3]}.")
print(f"The three items from the middle of the list are: {pizzas[1:4]}")
print(f"The last three items in the list are: {pizzas[-3:]}")

# Make a copy of the list and prove that the lists are different.

friend_pizzas = pizzas[:]

pizzas.append('Mediterranean')

friend_pizzas.insert(2, "pepperoni")

print(f"My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print(f"My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())