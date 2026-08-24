# Working with functions
# Scenario used in this lesson: You work in an IT support team for a tech 
# company. 

def print_separator():
    print("\n----------\n")

# ==============================================================================
# DEFINING A CUSTOM FUNCTION 
# ==============================================================================
# * Don't Repeat Yourself (DRY)-- if you find yourself writing the same code 
#   multiple times, write a function for it 
# * def function_name(arguments):
#       actions here 

# ------Examples: Defining Custom Functions------

# As part of an IT support team, you frequently convert employee names into 
# company email addresses with the standard format: 
# firstname.lastname@techcompany.com. Write a function to automate this task. 

full_name = "Alan Turing"

# Define the generate_email function 
def generate_email(full_name): 
    name_parts = full_name.split() #
    email = name_parts[0].lower() + '.' + name_parts[1].lower() + '@techcompany.com'

    # Return the email address
    return email 

# Call the function on the full_name string
# Expected: alan.turing@techcompany.com
print(generate_email(full_name))
print("\n----------\n")

# Given a list of test execution times, create a function that prints a report 
# showing the total number of tests and total test execution time. 
test_durations = [245.50, 189.99, 312.75, 156.20, 428.90, 201.35, 167.80]

def test_report(durations):
    # Calculate number of tests and total test time
    num_tests = len(durations)
    total_time = sum(durations)

    # Print report 
    print("=== Test Report ===")
    print("Total Tests: ", num_tests)
    print("Total Execution Time (s): ", total_time)

# Generate a report for recent test runs 
# Expected output-- 
# === Test Report ===
# Total Tests: 7
# Total Execution Time (s): 1702.49
print(test_report(test_durations))
print("\n----------\n")


# Your team is developing an authentication system for a website. Create a 
# function that validates passwords, verifying if the password is at least eight
# characters long and has at least one special character. 
import string

# sample password for testing
user_password = "SecurePass123!"

# Input: a string password
# Returns True if the password meets security requirements (8+ characters long 
# and contains at least one special character), returns False if it doesn't. 
def validate_password(password): 
    # Check if password is at least 8 characters long
    if len(password) >= 8:
        # Check if password contains a special character
        for char in password:
            if char in string.punctuation:
                return True
    return False 

# Call the function and store the result 
is_valid = validate_password(user_password)

# Expected output--
# "Is the password valid?  True"
print("Is the password valid? ", is_valid)
print("\n----------\n")

# ==============================================================================
# DEFAULT AND KEYWORD ARGUMENTS
# ==============================================================================
# * argument = a value passed (provided) to a function
# * positional argument = comma-separated arguments passed in order 
#   function_name(x, y)
# * keyword arguments = arguments assigned to keywords
#   function_name(number=x, ndigits=y)
#   * adds clarity
#   * can define function with default arguments 
# * To get a function's keyword arguments: print(help(function_name))

# ------Examples: Defining Custom Functions------

# Create a clean_text() function that takes a string, replaces spaces with 
# underscores, and optionally converts text to lowercase.
product = 'Wireless Mouse'

# Define clean_text function 
def clean_text(text, lower=True):
    clean_text = text.replace(' ', '_')
    if lower == False:
        return clean_text
    else:
        # Apply lowercase transformation
        return clean_text.lower()

# Test with default behaviour
# Expected output: "wireless_mouse"
print(clean_text(product))

# Alex's test for modifying default behaviour
# Expected output: "Wireless_Mouse"
print(clean_text(product, lower=False))
print_separator()


# You're building a feature that calculates discounted prices for an online
# store. You want to be able to set different discount amounts and control 
# whether prices are rounded to look cleaner in the app. 
# Create a function that takes a price and returns the price discounted by the 
# given percentage (default 15%) and optionally rounds it to two decimal places.

# Define the function with default arguments 
def calculate_discount(price, discount_percent=15, round_result=True):
    discounted_price = price - (price * (discount_percent / 100))

    if round_result == True:
        # Round the result to two decimal places 
        return round(discounted_price, ndigits=2)
    else:
        return discounted_price

# Call the function with keyword arguments 
original_price = 899.99
final_price = calculate_discount(price=original_price, discount_percent=25, 
                                 round_result=False)

# Expected output: 674.9925 (maybe slightly off depending on how floats are 
# calculated)
print(final_price)
print_separator()

# ==============================================================================
# DOCSTRINGS
# ==============================================================================
# * docstring = text describing what a function does, displayed when using 
#   help()
# * To access a docstring: my_function.__doc__ --> gets the docstring only 
#   * P.S: __ = "dunder"
#   * .__doc__ = "dunder-doc attribute"
# * To create a docstring: 
#   def my_function():
#       """Put docstring here""" 
#       OR 
#       """
#       Put multi-line docstring here. This part is a brief description of the 
#       function. 
#
#       Args: 
#           arg1 (data type): Describe what this argument is.
#           arg2 (data type): Describe what this argument is. 
#
#       Returns: 
#           return_variable (data type): Describe the value that is returned. 
#       """
# * To modify a docstring: my_function.__doc__ = "New docstring here"

# ------Examples: Docstrings------

# Take calculate_discount() and add a docstring stating "Calculate the 
# discounted price of a product" as if you were defining it for the first time.

def calculate_discount(price, discount_percent=15, round_result=True):
    # Add a single-line docstring:
    """Calculate the discounted price of a product.""" 

    discounted_price = price - (price * (discount_percent / 100))

    if round_result == True: 
        return round(discounted_price, ndigits=2)
    else:
        return discounted_price

# Access calculate_discount()'s docstring. 
# Expected output: Calculate the discounted price of a product. 
print(calculate_discount.__doc__)


# Take clean_text(). As if defining it for the first time, create it 
# with a multi-line docstring per the following specs: 
# Summary: Clean text by swapping spaces to underscores and converting to 
# lowercase.
# Arguments: 
# 1.) text (str): A string to be cleaned. 
# 2.) lower (bool): Whether to convert the text to lowercase. 
# Returns: text(str): Cleaned string. 

def clean_text(text, lower=True):
    # Add a multi-line docstring
    """
    Clean text by swapping spaces to underscores and converting to lowercase.
    
    Args:
        text (str): A string to be cleaned. 
        lower (bool): Whether to convert the text to lowercase. 

    Returns:
        text (str): Cleaned string. 
    """
    clean_text = text.replace(' ', '_')
    if lower == False:
        return clean_text
    else:
        return clean_text.lower()

# Access clean_text()'s docstring. 
print(clean_text.__doc__)
print_separator()

# ==============================================================================
# ARBITRARY ARGUMENTS
# ==============================================================================
# * arbitrary arguments = when a function accepts ANY number of arguments 
#   (positional, non-keyword)
# * def my_funct(*args): --> accepts arbitrary positional arguments 
#       * All arguments are combined into a single tuple
#       * "*args" is conventional, but could technically put * + anything
# * my_funct(*[a, b], *[c, d], *[x, y]) --> combines multiple lists into one 
#   structure that can be passed into my_funct() together
# * def my_funct(**kwargs) --> accepts arbitrary keyword arguments
#       * All keyword=value arguments are combined into a single dictionary
#       * "**kwargs" is conventional, but ** + anything works too
# * my_funct(**{"a":1, "b":2}, **{"c":3, "d":4}, **{"e":5, "f":6}) --> passes 
#   each dictionary as keyword argument ("kwargs") and maps each key-value pair 
#   to its own keyword=value pair

# ------Examples: Arbitrary Arguments------

# Create a function that concatenates an arbitrary number of strings together
# with spaces between each one. 

def concat(*args):
    """
    Concatenates multiple string arguments with spaces between them.
    
    Args: 
        *args (str): Strings to concatenate. 

    Returns: 
        result(str): All strings put together with spaces in between. 
    """

    result = ""

    for arg in args:
        result += " " + arg

    return result 

# Test-- expected output: " Python is great!"
print(concat("Python", "is", "great!"))
print_separator()

# Modify the concat() function above-- redefine it as a function that accepts 
# arbitrary keyword arguments.
def concat(**kwargs):
    """
    Concatenates keyword arguments into a single string with spaces
    
    Args: 
        *kwargs (str): Strings to concatenate. 

    Returns: 
        result(str): All strings put together with spaces in between. 
    """

    result = ""

    for kwarg in kwargs.values():
        result += " " + kwarg

    return result 

# Expected output: " Python is great!"
print(concat(start="Python", middle="is", end="great!"))
print_separator()