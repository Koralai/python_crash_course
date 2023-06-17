# Continue adding toppings to a pizza until the user is done ordering.

prompt = 'What topping would you like to add to your pizza? '
prompt += "Enter 'done' to finish ordering. "


while True:
    toppings = input(prompt)
    
    if toppings.lower() == 'done':
        break
    else:
       print(f'Great choice! Adding {toppings.lower()} to your pizza.') 