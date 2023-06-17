
from datetime import datetime


class Person:
    """A simple model of a person."""
    
    def __init__(self, first_name: str, last_name: str, birth_year: int, deceased_year: int=None):
        """Initial attributes: first name, last name, birth year"""
        
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.deceased_year = deceased_year
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_age(self) -> int:
        if self.deceased_year is None:
            current_year = datetime.now().year
            return current_year - self.birth_year
        return self.deceased_year - self.birth_year
        
    def __str__(self) -> str:
        if self.deceased_year is None:
            return f'{self.get_full_name()} is a person who is {self.get_age()} years old.'
        return f'{self.get_full_name()} passed away at the age of {self.get_age()}.'
    
        

def main():
    person = Person('Carrie', 'Clarky', 1988)
    print(person)

if __name__ == '__main__':
    main()
