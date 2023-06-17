# Create a list of people I'd like to have for dinner.

dinner_guests = ['hypatia', 'socrates', 'michael sandel']

# Create an invitation message and print it for each person.

invitation_message = "I hope you'll join us for an evening of good food, fine wine, and delectable conversation."

print(f'{dinner_guests[0].title()}, {invitation_message}')
print(f'{dinner_guests[1].title()}, {invitation_message}')
print(f'{dinner_guests[2].title()}, {invitation_message}')

# Socrates can't make it. Replace him on the guest list and send out a new set of invitations.

not_attending = 'socrates'
dinner_guests.remove(not_attending)

print('\n')
print(f"{not_attending.title()} sends their deepest regrets and won't be able to attend.")

dinner_guests.insert(1, 'epicurus')

print('\n')
print(f'{dinner_guests[0].title()}, {invitation_message}')
print(f'{dinner_guests[1].title()}, {invitation_message}')
print(f'{dinner_guests[2].title()}, {invitation_message}')

# Invite three more guests to dinner.

print('\n')
print("Good news! We found a bigger table and can add more people to our dinner party.")

dinner_guests.insert(0, 'ada lovelace')
dinner_guests.insert(3, 'henry david thoreau')
dinner_guests.append('seneca')

print('\n')
print(f'{dinner_guests[0].title()}, {invitation_message}')
print(f'{dinner_guests[1].title()}, {invitation_message}')
print(f'{dinner_guests[2].title()}, {invitation_message}')
print(f'{dinner_guests[3].title()}, {invitation_message}')
print(f'{dinner_guests[4].title()}, {invitation_message}')
print(f'{dinner_guests[5].title()}, {invitation_message}')

# Cut four people from the guest list and apologize to each one.

print('\n')
print("So, so sorry! It turns out the new table won't arrive in time, and we only have room for two guests.")

uninvited = dinner_guests.pop()
print(f"I'm so sorry, {uninvited.title()}, but you'll have to dine with us another time.")

uninvited = dinner_guests.pop()
print(f"I'm so sorry, {uninvited.title()}, but you'll have to dine with us another time.")

uninvited = dinner_guests.pop()
print(f"I'm so sorry, {uninvited.title()}, but you'll have to dine with us another time.")

uninvited = dinner_guests.pop()
print(f"I'm so sorry, {uninvited.title()}, but you'll have to dine with us another time.")

# Invite the remaining two guests.

print('\n')
print(f"Now, for sure, {len(dinner_guests)} people can attend this party.")
print(f"{dinner_guests[0].title()} and {dinner_guests[1].title()}, you're still invited if you'd like to come.")

# Empty out the list of dinner guests.

del dinner_guests[0]
del dinner_guests[0]

print(dinner_guests)

