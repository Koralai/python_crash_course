class QuizQuestion:
    """A simple model of a quiz question with three answers"""
    
    def __init__(self, question: str, answers: list):
        """Initial attributes for the question and a list of answers"""
        self.question = question
        self.answers = answers
    
    def structure_question(self):
        """Store question and answers in a dictionary"""
        new_question = {}
        answer_lett = 'a'
        
        new_question['question'] = self.question
        for answer in self.answers:
            new_question['ans_' + answer_lett] = answer
            # Advance to the next answer letter (e.g., a, b, c)
            answer_lett_ascii_value = ord(answer_lett)
            answer_lett_ascii_value += 1
            answer_lett = chr(answer_lett_ascii_value)
            
        return new_question
            
    def calculate_score(self, user_input):
        """Calculate the score based on the user's supplied answer"""
        
        if user_input.lower() == 'a':
            score = 0
            return score
        elif user_input.lower() == 'b':
            score = 1
            return score
        elif user_input.lower() == 'c':
            score = 2
            return score
        else:
            # The function evaluates to false if the input is invalid
            return False

# Future improvement:
# Make the code more flexible, to allow for a variable number of answers
    # This affects .calculate_score()
