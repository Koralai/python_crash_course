# Create a list of favorite foods. 
# Copy the list and add something different to each version. 

my_foods = ['pizza', 'pasta', 'ice cream']
hubby_foods = my_foods[:]

my_foods.append('bagels')
hubby_foods.append('fish and chips')

# Print the two lists.

print("My favorite foods are:") 
for food in my_foods:
    print(food.capitalize())

print("\nJon's favorite foods are:")
for food in hubby_foods:
    print(food.capitalize())