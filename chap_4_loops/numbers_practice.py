# Use a for loop to print the numbers from 1 to 20, inclusive

for value in range(1, 21):
    print(value)

# Print the numbers from 1 to 1 million, using steps of 250.

big_list = []

for value in range(1, 1_000_000, 250):
    big_list.append(value)

print(big_list)