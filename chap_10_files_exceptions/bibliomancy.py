"""Reads a text file and returns a random sentence"""

from pathlib import Path
from random import randint

def get_text_from_file(file): 
    """Returns the text contained in a file"""   
    # Specify encoding for files from external sources
    return Path(file).read_text(encoding='utf-8')

def lines_to_string(text):
    """Converts lines of text into a single string"""
    new_string = ''
    for line in text.splitlines():
        # .splitlines() turns the text into a list, with each line as an item
        new_string += f" {line.strip()}" 
        
    return new_string

def random_sentence(text):
    """Takes a string and extracts a random sentence from it"""
    str_length = len(text)
    # Find the length of the string
    
    finding_index = True
    while finding_index is True:
        
        random_index = randint(0, (str_length-1))
        # Pick a random index within the string's length
        
        while text[random_index] not in ['.', '!', '?']:
            # Start at this index and loop until you find the end of a sentence
            random_index += 1
        if random_index != str_length - 1:
            # If this would be past the last index (last sentence), start over
            finding_index = False

    if text[random_index + 2] == '.':
        # Handle ellipses
        starting_index = random_index + 4
    else:
        starting_index = random_index + 2
        # Otherwise, the random index +2 is the new starting index
    
    sentence = ''
    working_index = starting_index
    
    while text[working_index] not in ['.', '!', '?']:
        # Starting from the new index, add characters to the empty string 
        # Keep going until you encounter the end of a sentence
        sentence += f"{text[working_index]}"
        working_index += 1
    sentence += f"{text[working_index]}"
    # Add the last punctuation mark
        
    return sentence.strip()
    # Strip any whitespace
    
def bibliomancy(file):
    """
    Combines all bibliomancy steps into one function call
    and handles 'file not found' errors
    """
    try:
        new_text = get_text_from_file(file)
    except FileNotFoundError:
        print(f'Sorry, the file {file} does not exist.')
    else:
        new_string = lines_to_string(new_text)
        return random_sentence(new_string)

        
def main():
    print(bibliomancy('little_women.txt'))

if __name__ == '__main__':
    main()


# Future improvements:
    # Handle "Mr.", "Mrs." "Ms."
    # "String out of range" error persists
