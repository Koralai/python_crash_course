class Employee:
    """A simple model of an employee"""
    
    def __init__(self, first_name, last_name, salary):
        """Initial attributes for first name, last name, and salary"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        
    def give_raise(self, amount=5000):
        """Increase the salary by $5,000 by default, or any other amount"""
        new_salary = self.salary + amount
        return new_salary
