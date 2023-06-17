# Take a number from the user and tell them if it's a multiple of ten.

user_number = input("Name any number. I'll tell you if it's a multiple of ten. ")
user_number = int(user_number)

if user_number % 10 == 0:   # No remainder if dividing by 10 = divisible by 10
    print(f'The number {user_number} is a multiple of ten.')
else:
    print(f'The number {user_number} is not a multiple of ten.')