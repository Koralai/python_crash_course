import random   # Needed for later functionality

class Philosopher:
    """A model of a philosopher"""
    
    def __init__(self, first_name: str, last_name: str, interests: list[str], sex: str):
        """Initial attributes for name, fields of interest, and sex."""
        self.first_name = first_name
        self.last_name = last_name
        self.interests = interests
        self.sex = sex

    def get_pronouns(self) -> list[str]:
        """Get appropriate pronouns to use in text about the philosopher."""
        if self.sex.lower() == 'female':
            return ['she', 'her', 'her']
        else:
            return ['he', 'him', 'his']
     
    def get_full_name(self) -> str:
        """
        Return the philosopher's name with proper formatting.
        Account for the fact that some philosophers only have a first name.
        """
        if self.last_name == '':
            return f"{self.first_name.title()}"
        return f"{self.first_name.title()} {self.last_name.title()}"

    def describe_philosopher(self) -> None:
        """Print a simple describe of the philosopher and their work."""
        print(
                f"{self.get_full_name()} is known for "
                f"{self.get_pronouns()[2]} work in the following fields:" 
            )
        for interest in self.interests:
            print(f"- {interest.capitalize()}")
            
    def give_speech(self) -> None:
        """Simulates the philosopher giving a speech on one of their intersts."""
        speech_topic = random.choice(self.interests)
        # Random item from the list of interests
        print(f"{self.get_full_name()} is giving a speech on {speech_topic}.")

        
phil_1 = Philosopher(
            'peter', 'singer', 
            [
                'ethics', 'utilitarianism', 
                'effective altruism', 'animal rights'
            ],
            'male'
    )
phil_1.describe_philosopher()
phil_1.give_speech()

phil_2 = Philosopher(
        'philippa', 'foot',
        ['virtue ethics', 'Aristotle', 'the trolley problem'],
        'female'
)
phil_2.describe_philosopher()
phil_2.give_speech()

phil_3 = Philosopher(
        'plato', '',
        ['political philosophy', 'metaphysics', 'philosophical dialogues'],
        'male'
)
phil_3.describe_philosopher()
phil_3.give_speech()
