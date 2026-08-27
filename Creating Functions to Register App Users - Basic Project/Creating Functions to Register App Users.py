# TO DO: figure out why my docstrings aren't working T_T

# You are a junior developer working in a small start-up. Your managers have 
# asked you to develop a new account registration system for a mobile app. The 
# system must validate user input on the sign-up form before creating an 
# account. 

# The previous junior developer wrote some helper functions that validate the 
# name, email, and password. Use these functions to register users, store their 
# data, and implement some error handling! These have been imported into the 
# workspace for you. They will be a great help to you when registering the user, 
# but first you have to understand what the function does! Inspect the 
# docstrings of each of the helper functions: `validate_name`, `validate_email` 
# and `validate_password`.

# Run this cell and examine the docstring of each function
from python_functions import validate_name, validate_email, validate_password, top_level_domains

print("validate_name\n")
print(validate_name.__doc__)
print("--------------------\n")

print("validate_email\n")
print(validate_email.__doc__) 
print("--------------------\n")

print("validate_password\n")
print(validate_password.__doc__)

# The top level domains variable is used in validate_email to approve only 
# certain email domains
print(top_level_domains)

# Create a validate_user() function, using some helper validation functions to 
# verify user input.
#   * The function should take in the parameters: name, email, and password.
#   * The function should call each of the helper validation functions 
# (validate_name(), validate_email(), and validate_password()).
#   * If any check fails, raise a ValueError with a descriptive error message 
#     about the failing validation.
#   * If all checks pass, return True. 

def validate_user(name: str, email: str, password: str) -> bool:
    """
    Validates user information. 

    Args: 
        name (str): The user's name. 
        email (str): The user's email address.  
        password (str): The user's password. 

    Returns:
        bool: True if all user information meets validation requirements.
    """

    if validate_name(name) == False:
        raise ValueError("Invalid name. Names must be be a string greater than two characters.")
    elif validate_email(email) == False:
        raise ValueError("Invalid email. Emails must have a username greater than 1 character, an '@' symbol, and an allowed domain that is in the `top_level_domains` variable.")
    elif validate_password(password) == False:
        raise ValueError("Invalid password. Passwords must include a capital letter, include a number between 0-9, and be greater than 8 characters.")
    else:
        return True

# Test validate_user()
# (will only print to console if a test shows something is wrong)
def test_validate_user() -> None:
    valid_name = "Alex"
    valid_email = "alex@domain.net"
    valid_password = "Password123"

    # helper function for testing invalid inputs-- if validate_user() raises 
    # a ValueError as expected, then this should pass. Otherwise, raise an 
    # AssertionError.  
    def test_invalid_user(name=valid_name, email=valid_email, password=valid_password): 
        try:
            # expected behaviour: raises ValueError for except block to catch 
            assert validate_user(name, email, password) is True
        except ValueError:
            pass

    # happy path-- all inputs are valid
    assert validate_user(valid_name, valid_email, valid_password) is True

    # invalid inputs
    test_invalid_user(name="a")
    test_invalid_user(email="a")
    test_invalid_user(password="a")

    # null case
    test_invalid_user(name="", email="", password="")

# Now that you've validated that all the user details are correct, you want to 
# allow users to register to the app. Create a register_user() function to 
# handle the registration logic.

# The function should take in the parameters: name, email, and password.
# Inside, it should call validate_user() to ensure that the user input is valid.
# If validate_user() raises a ValueError, register_user() should catch the 
# exception and return False.
# Otherwise, it should create and return a dictionary with the keys: name, 
# email, and password.

def register_user(name: str, email: str, password: str) -> dict|bool:
    """
    Registers a user to the app. 
       
    Args: 
        name (str): The user's name.
        email (str): The user's email address. 
        password(str): The user's password.  

    Returns: 
        dict: If successful, returns this user's information. 
        bool: Returns False if any of the user's details contained invalid inputs. 
    """

    try:
        validate_user(name, email, password)
        return {"name": name,
                "email": email, 
                "password": password}
    except ValueError: 
        return False

# Tests for register_user()
def test_register_user():
    valid_name = "Alex"
    valid_email = "alex@domain.net"
    valid_password = "Password123"

    # happy path 
    assert register_user(valid_name, valid_email, valid_password) == {"name": valid_name,
                                                                      "email": valid_email,
                                                                      "password": valid_password}

    # invalid inputs
    assert register_user("a", valid_email, valid_password) is False
    assert register_user(valid_name, "a", valid_password) is False
    assert register_user(valid_name, valid_email, "a") is False

    # null invalid inputs
    assert register_user("", "", "") is False 
    
test_register_user()