from pathlib import Path

path = Path('guest.txt')

guest_name = input('What is your name? ')

path.write_text(guest_name)