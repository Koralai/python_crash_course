from question_letters import get_answer_letters

def test_question_letters():
    """Do 4-answer questions work?"""
    
    # given
    answers = [
        'cherry', 'peach', 'banana cream', 'key lime'
    ]
    
    # when
    answer_letters = get_answer_letters(answers)
    
    # then
    assert answer_letters == ['a', 'b', 'c', 'd']
