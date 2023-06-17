from quiz_question import QuizQuestion
import pytest

# given

@pytest.fixture
def new_question():
    """A quiz question that will be available for all tests"""
    question = 'Which of these is closest to your dream home?'
    answers = [
        'A brownstone next to Central Park in New York City',
        'A cottage in the countryside',
        'An old house overlooking the sea'
    ]
    
    new_question = QuizQuestion(question, answers)
    return new_question

def test_quiz_question_structure(new_question):
    """Make sure the quiz question is stored in a proper data structure"""

    # when
    new_question_data = new_question.structure_question()
    
    # then
    assert new_question_data['ans_b'] == 'A cottage in the countryside'

def test_quiz_question_answer(new_question):
    """Make sure the user's answer is properly scored"""

    # when
    user_answer = 'b'
    question_score = new_question.calculate_score(user_answer)    
    
    # then
    assert question_score == 1

def test_quiz_question_invalid_input(new_question):
    """Make sure .calculate_score() is false if the user's answer is invalid"""

    # when
    user_answer = 'f'
    question_score = new_question.calculate_score(user_answer)
    
    assert question_score is False
