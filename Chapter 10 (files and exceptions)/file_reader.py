from pathlib import Path

def main():

    path = Path('pi_digits.txt')
    # Make sure you are in the correct working directory, or this won't work
    contents = path.read_text()

    pi_string = ''
    for line in contents.splitlines():
        # splitlines() creates a list containing each line of text
        pi_string += line.lstrip()
    print(pi_string)
    print(len(pi_string))
    
    # path_2 = Path('../Projects/program_ideas.txt')
    # # This path moves up one folder and into a different folder
    # contents_2 = path_2.read_text()
    # print(contents_2)

if __name__ == '__main__':
    main()
