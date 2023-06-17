"""Reads a file and prints its contents. Handles 'file not found' errors."""

from pathlib import Path

def print_file(file):
    try:
        new_text = Path(file).read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"The file {file} does not exist.")
    else:
        print(new_text)

def main():
    print_file('dogs.txt')
    print_file('cats.txt')
    print_file('rabbits.txt')

if __name__ == '__main__':
    main()
