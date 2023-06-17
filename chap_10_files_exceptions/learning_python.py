"""
Get text about learning Python from another file.
Convert it to a single, formatted string.
"""

from pathlib import Path

def main():
    # Locate the text file
    path = Path('learning_python.txt')
    # Store its contents in a variable
    contents = path.read_text()
    
    # Combine the original lines of text into one string
    message = ''
    for line in contents.splitlines(): 
        message += (f"{line} ") # Add space between each line
    print(message)

if __name__ == '__main__':
    main()
