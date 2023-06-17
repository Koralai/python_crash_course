def get_answer_letters(answers: list):
    """
    Return letters corresponding with answers to a multiple-choice question
    (a, b, c, etc)
    """
    ascii_counter = 97 # Start at ASCII value 'a'
    answer_letters = []
    for _ in answers:
        answer_letters.append(chr(ascii_counter))
        ascii_counter += 1
    
    return answer_letters
