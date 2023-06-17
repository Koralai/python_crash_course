from pathlib import Path
import json

def register_user(path):
    """Prompt for new user info. Store the info in a json file."""
    print("\nPlease provide this information to create an account:")
    user_info = {}

    user_info['username'] = input("Username: ")   
    user_info['first name'] = input("First name: ")    
    user_info['last name'] = input("Last name: ")        
    user_info['email'] = input("Email address: ") 
    user_info['bio'] = input("A short bio of yourself: ")

    user_info_json = json.dumps(user_info)
    Path(path).write_text(user_info_json)
    
    return user_info    
        
def get_stored_user_info(path):
    """Retrieve stored user info from a json file, if it exists."""
    if path.exists():
        json_contents = path.read_text()
        user_info = json.loads(json_contents)
        return user_info
    return None

def display_user_info():
    """
    Show user info, if available and if it matches the current user. 
    If not, register the user.
    """
    user_info_file = Path('user_data.json')
    current_user = get_stored_user_info(user_info_file)
    
    # If any user exists, verify it is the correct user.
    # If not, register a new user.    
    if current_user:
        while True:
            verify_user = input(f"Is your username {current_user['username']}? (y/n) ")
            if verify_user.lower() == 'y':
                break
            elif verify_user.lower() == 'n':
                current_user = register_user(user_info_file)
                break
            else:
                print("Please answer 'y' or 'n'.")
        print(f"\nWelcome back, {current_user['first name'].title()}! Your info:\n")
        for key, value in current_user.items():
            print(f"{key.title()}: {value}")
    
    # If no user exists, register a new user.
    else:
        register_user(user_info_file)


display_user_info()
