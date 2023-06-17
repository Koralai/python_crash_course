"""A class that represents a user"""

class User:
    """A basic model of a user."""
    
    def __init__ (
                self, first_name, last_name, 
                birth_year, email, display_name
        ):
        """Initialize with basic user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.email = email
        self.display_name = display_name
        self.login_attempts = 0
        
    def describe_user(self):
        """Summarize the user's information."""
        print(
                f"First name: {self.first_name.title()}\n"
                f"Last name: {self.last_name.title()}\n"
                f"Birth year: {self.birth_year}\n"
                f"Email address: {self.email}\n"
                f"Display name: {self.display_name}"
            )
    
    def greet_user(self):
        """Display a personalized greeting for the user."""
        print(
                f"Hi {self.first_name.title()}! "
                f"You are logged in as {self.display_name}. "
                "Have a great day!"
            )
        
    def increment_login_attempts(self):
        """Record a new login attempt."""
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """Reset the number of login attempts to zero."""
        self.login_attempts = 0
