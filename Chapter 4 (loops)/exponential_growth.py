# This code creates a list of numbers starting at 1 and doubling at each step.

# Create an empty list to populate.
# Create a variable with an initial value. 

exponential_growth = []
number = 1

# Inside a for loop:
    # Double the initial value. Update the variable to store this new number.
    # Add this number to the list.
# "_" is a counter for how many times the loop runs; not used inside the loop.

for _ in range(number, 21):
    number = number*2
    exponential_growth.append(number)

# Print the populated list.

print(exponential_growth)
