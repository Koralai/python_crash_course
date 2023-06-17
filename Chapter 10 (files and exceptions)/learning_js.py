from pathlib import Path

def main():
    path = Path('learning_python.txt')
    contents = path.read_text()
    
    message = ''
    for line in contents.splitlines():
        message += (f"{line} ") # Adds space between each line
    print(message)
    
    # Replace the word 'Python' with 'Javascript'
    new_message = message.replace('Python', 'Javascript')
    print(new_message)

if __name__ == '__main__':
    main()
