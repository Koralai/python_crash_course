"""A class that represents a restaurant"""

class Restaurant:
    """A basic model of a restaurant"""
    
    def __init__(self, name, cuisine_type):
        """Initialize with name and cuisine attributes."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Write a basic tagline for the restaurant."""
        print(f"We are {self.name}, experts in "
              f"{self.cuisine_type} cuisine.")
        
    def open_restaurant(self):
        """Simulate the restaurant opening for the day."""
        print(f"{self.name} is open for business today.")
    
    def set_number_served(self, number):
        """Modify the attribute for number of customers served."""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can't subtract people you've already served!")
    
    def increment_number_served(self, number):
        """Update the number of customers served."""
        self.number_served += number
