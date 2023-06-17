"""A set of classes that represent admins and their privileges"""

from user import User

class Admin(User):
    """Model for an admin, a subclass of user."""
    
    def __init__(
                self, first_name, last_name, 
                birth_year, email, display_name 
                 ):
        """Initialize with regular user attributes plus admin privileges."""
        super().__init__(
                first_name, last_name, birth_year, 
                email, display_name
            )
        self.privileges = Privileges()
        
class Privileges:
    """Stores admin privileges and related methods."""
    
    def __init__(
                self, 
                privileges=[
                    'can add post', 'can delete post', 
                    'can ban user', 'can move thread',
                    'can lock thread'                    
                ]
        ):
        """
        Initialize with an attribute for privileges.
        The default privileges are already specified.
        """
        self.privileges = privileges
        
    def show_privileges(self):
        """Show the admin's privileges."""
        
        print("Available admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege.capitalize()}")


# user_04 = Admin(
#             'helga', 'longworth', 1998,
#             'hlongworth@gmail.com', 'gigi98'
# )

# user_04.greet_user()
# user_04.privileges.show_privileges()
