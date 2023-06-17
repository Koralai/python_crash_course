class Restaurant:
    """A basic model of a restaurant."""
    
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
        

class IceCreamStand(Restaurant):
    """Model an ice cream stand, a child of the restaurant class."""
    
    def __init__(self, name, cuisine_type, flavors):
        """
        Initialize with attributes of the parent class, plus available flavors.
        """
        # Not sure what to do with cuisine_type since I don't really need it for this subclass.
        super().__init__(name, cuisine_type)
        self.flavors = flavors
        
    def display_flavors(self):
        """Show a list of available flavors, in alphabetical order."""
        print(f"Flavors available: ")
        for flavor in sorted(self.flavors):
            print(f"- {flavor.capitalize()}")
            
new_icecream_shop = IceCreamStand(
            "Joey's Ice Cream Palazzo",
            "American",
            [
                'coffee', 'vanilla', 'chocolate',
                'strawberry', 'fudge tracks', 'mint chip',
                'butter pecan', 'cookie dough', 'bubblegum'
            ]
)

new_icecream_shop.display_flavors()