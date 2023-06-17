# Make a list of the cubes of the numbers 1 to 10.

list_of_10 = []

for value in range(1, 11):
    value = value**3
    list_of_10.append(value)
    print(value)
    
print(list_of_10)

# Do the same thing with a list comprehension.

cubes = [value**3 for value in range(1, 11)]
print(cubes)