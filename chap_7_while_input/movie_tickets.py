# Ask for the user's age. Tell them the price of their movie ticket,
# based on their age.

prompt = 'Some people are eligible for age-related discounts. How old are you? '
prompt += '\nEnter "done" to finish your order. '

ordering = True

while ordering:
    age = input(prompt)
    
    if age.lower() == 'done':
        ordering = False
    else: 
        age = int(age)
        if age < 3:
            print('Your ticket is free!')
        elif age < 12:
            print ('Your ticket will be $10.')
        else:
            print('Your ticket will be $15.')
        