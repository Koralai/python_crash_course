"""
Prints the first 50 digits of pi, from a txt file with the first million digits.
"""

from pathlib import Path

def main():
    path = Path('pi_million_digits.txt')
    contents = path.read_text()
    
    pi_string = ''
    for line in contents.splitlines():
        pi_string += line.lstrip()
        
    print(f"{pi_string[:52]}...")
    print(len(pi_string))

if __name__ == '__main__':
    main()
