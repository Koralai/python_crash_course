"""Adds two numbers together"""

print("Enter two numbers, and I'll add them together.\n")
print("Press 'q' at any time to quit.\n")

while True:
    num_1 = input("First number: ")
    if num_1.lower() == 'q':
        break

    num_2 = input("Second number: ")
    if num_2.lower() == 'q':
        break
    
    try:
        num_sum = int(num_1) + int(num_2)
    # Handle invalid inputs:
    except ValueError:
        print("Both values should be numbers. Please try again.\n")
    else:
        print(num_sum)
