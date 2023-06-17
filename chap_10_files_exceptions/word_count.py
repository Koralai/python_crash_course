from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file"""

    try:
        contents = path.read_text(encoding='utf-8')
        # Specify encoding for files from external sources
    except FileNotFoundError:
        # print(f"Sorry, the file {path} does not exist.")
        pass
    else:
        # Count the apprxomate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words:,} words.")


def main():

    filenames = ['alice.txt', 'siddhartha.txt', 
                 'moby_dick.txt', 'little_women.txt']
    
    for filename in filenames:
        path = Path(filename)
        count_words(path)

if __name__ == '__main__':
    main()
