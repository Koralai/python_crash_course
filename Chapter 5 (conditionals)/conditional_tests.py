# Come up with 10 or more conditional tests.

poets = ['Auden', 'Shakespeare', 'Dickinson', 'Crane', 'Stephens', 'Hughes']
poets.sort()

print("Is Auden listed first now? I predict True.")
print(poets[0].lower() == 'auden')

print("So is Shakespeare *not* first in the list? I predict True.")
print(poets[0].lower() != 'shakespeare')

print("Is Plath on the list? I predict False.")
print('Plath' in poets)

print("Who is last on the list now? I think it's Stephens. Let's check.")
print(poets[-1].lower() == 'stephens')

print("Are both Dickinson and Rossetti on the list? I predict False.")
print('Dickinson' and 'Rossetti' in poets)

print("Did I forget to put Whitman on the list? I predict True.")
print("Whitman" not in poets)

birth_year_1 = 1899
birth_year_2 = 1905
birth_year_3 = 1946
birth_year_4 = 1983
current_year = 2023

print("Was the first person born before 1900? I predict True.")
print(birth_year_1 < 1900)

print("Is the last person younger than 50? I predict True.")
print((current_year - birth_year_4) < 50)

print("Was either the second or third person born after WWII? I predict True.")
print(birth_year_2 > 1945 or birth_year_3 > 1945)

print("Would the first two people be older than 100 this year? I predict True.")
print(
    (current_year - birth_year_1) >= 100 
    and 
    (current_year - birth_year_2) >= 100)

print("2022 is in the past, right? I predict True.")
print(current_year != 2022)

print("So, it's 2023, right? I predict True.")
print(current_year == 2023)