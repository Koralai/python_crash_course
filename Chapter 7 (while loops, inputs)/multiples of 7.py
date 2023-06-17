# Practicing with the term 'continue'

# Set an initial value

current_number = 0

# Increment the value by 1 for each number from 1 to 150. 
# Only print numbers that are multiples of 7.

while current_number < 150:
    current_number += 1
    if current_number % 7 != 0:
        continue    # If it's not divisible by 7, restart the loop here.
    print(current_number)