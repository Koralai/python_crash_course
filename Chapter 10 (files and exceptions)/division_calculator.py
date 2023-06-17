"""
Takes two numbers and divides the first by the second.
Handles a user's attempt to divide by zero.
"""

print("Give me two numbers, and I'll divide them.")
print('Enter "q" to quit.')

while True:
    first_number = input("\nFirst number: ")
    if first_number.lower() == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number.lower() == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
