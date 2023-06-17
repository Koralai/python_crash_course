# Create a list that holds the numbers from 1 to 1,000,000.

big_list = []

for value in range(1, 1_000_001):
    big_list.append(value)

# Print simple statistics about this list.

print(f"Minimum value: {min(big_list)}")
print(f"Maximum value: {max(big_list)}")
print(f"Sum of all values: {sum(big_list)}")