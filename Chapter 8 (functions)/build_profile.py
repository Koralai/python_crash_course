def build_profile(first, last, **user_info):
    """
    Build a dictionary containing a user's first name, last name, and
    any other info added during the function call.
    """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

new_user_1 = build_profile('carrie', 
                           'clark', 
                           freckles=True, 
                           activities=['cycling', 'walking', 'hiking'],
                           husband='jon')

print(new_user_1)