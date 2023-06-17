# Convert a list of plain numbers to ordinals.

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

numbers_ordinal = []

# Is type conversion happening here?

for number in numbers:
    if number == 1:
        numbers_ordinal.append(f'{number}st')
    elif number == 2:
        numbers_ordinal.append(f'{number}nd')
    elif number == 3:
        numbers_ordinal.append(f'{number}rd')
    else:
        numbers_ordinal.append(f'{number}th')
        
print(numbers_ordinal)