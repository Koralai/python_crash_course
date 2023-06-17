# Print the numbers from 1 to 5.

for value in range(1, 6):
    print(value)

# Save the numbers 1 through 5 in a list.
    
numbers = list(range(1, 6))
print(numbers)

# Print a list of even numbers between 1 and 10.

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Print a list of the first ten square numbers.

squares = []

for value in range(1, 11):
    squares.append(value ** 2)
    
print(squares)