# Create an unordered list of scores.

scores = [
    60,
    72,
    84,
    93,
    42,
    82,
    79
]

# Sort the scores from highest to lowest.

scores.sort(reverse=True)

# Print the highest/lowest 3 scores from this list.

print(f"The three highest scores are:")
for score in scores[:3]:
    print(score)

print(f"\nThe three lowest scores are:")
for score in scores[-3:]:
    print(score)