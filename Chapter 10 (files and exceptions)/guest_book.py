"""Builds a list of names and writes them to a text file"""

from pathlib import Path

def build_guest_book():
    collecting_names = True
    guest_names = ''

    while collecting_names is True:
        
        new_name = input('What name would you like to record? ')
        guest_names += f"{new_name}\n"
        # Add the new name to the string
        
        check_quit = input('Press q to quit, or any other key to enter another name. ')
        if check_quit.lower() == 'q':
            collecting_names = False
    
    return guest_names


def main():
    path = Path('guest_book.txt')
    path.write_text(build_guest_book())

if __name__ == '__main__':
    main()
