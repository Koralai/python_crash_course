"""Count particular words in a piece of text"""

from pathlib import Path

def count_words(file, word):
    """
    Reads a text file, counts the occurrences of a specific word in the file,
    and returns a message about the final count
    """
    # Try to read the text in the file
    try:
        path = Path(file)
        contents = path.read_text(encoding='utf-8')

    # Show an error message if the file can't be located    
    except FileNotFoundError:
        err_msg = f"The file {file} does not exist."
        return err_msg

    word_count = contents.lower().count(word)
    word_count_msg = f"The word '{word}' appears {word_count:,} times in {file}."
    return word_count_msg
    

def main():
    print(count_words('moby_dick.txt', 'whale'))
    print(count_words('emma.txt', 'friendship'))

if __name__ == '__main__':
    main()
