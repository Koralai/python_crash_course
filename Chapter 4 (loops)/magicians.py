# First time using a Python for loop

# Define a list of magicians to loop through.

magicians = ['alice', 'harry', 'david', 'nina']

# Loop through the list, printing a message for each magician.

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    
# Print one summary message after the loop has finished.
    
print("Thank you, everyone. That was great magic show.")
