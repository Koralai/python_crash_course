"""Determines if the user's birthday is in the first million digits of pi"""

from pathlib import Path

def main():
    # Store text from a file with the first million digits of pi
    path = Path('pi_million_digits.txt')
    contents = path.read_text()
    
    # Arrange the text into a single string
    pi_string = ''

    for line in contents.splitlines():
        pi_string += line.lstrip()
    
    # Check if user input can be found in the string
    birthday = input('Enter your birthday, in the form mmddyy: ')
    if birthday in pi_string:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Your birthday does not appear in the first million digits of pi.")

if __name__ == '__main__':
    main()
