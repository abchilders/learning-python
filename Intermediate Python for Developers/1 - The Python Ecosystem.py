# The Python Ecosystem
# Example used in this lesson: performance monitoring dashboard for food 
#    delivery app

# ==============================================================================
# BUILT-IN FUNCTIONS
# ==============================================================================
# * print("hello world") --> prints to screen
# * type(my_var) --> returns data type of my_var
# * range(x, y) --> generates list from x up to but not including y
# * max(my_list) --> returns largest value
# * min(my_list) --> returns smallest value
# * sum(my_list) --> returns sum of all values
# * round(my_num, num_decimals) --> rounds my_num to the given number of decimal
#   places
# * len(my_list) --> returns number of elements 
#       * len(my_string) --> number of characters
# * sorted(my_list) --> sorts from smallest to largest, or alphabetically

# ------Examples: Built-In Functions------
print("------Examples: Built-In Functions------")

# Order amounts from the past hour during peak traffic
recent_orders = [15.99, 28.50, 42.75, 18.99, 55.00, 31.25, 22.99, 67.50]

# Find the smallest order amount from the past hour 
smallest_order = min(recent_orders)

# Find the largest order amount
largest_order = max(recent_orders)

# Calculate total revenue from all orders in the last hour 
total_revenue = sum(recent_orders)

# Expected output-- 
# Smallest order: 15.99
# Largest order: 67.50
# Total revenue: 282.97
print("Smallest order:", smallest_order)
print("Largest order:", largest_order)
print("Total revenue:", total_revenue)


# Given a list of delivery times during peak dinner hours, calculate the average
# delivery time 
delivery_times = [19, 25, 35, 40, 28, 32, 29, 31]

average_time = sum(delivery_times) / len(delivery_times)

# Round the average delivery time to two decimal places 
average_rounded = round(average_time, 2)

# Expected output-- 
# Average delivery time: 29.88 
print("Average delivery time:", average_rounded)


# Sorting lists of restaurant names and average meal preparation times
restaurants = ["Sushi Central", "Burger Hub", "Taco Town", "Pizza Palace"]
cooking_times = [30, 25, 35, 40, 28, 32, 29, 31, 12, 55]

# Sort restaurant names alphabetically
restaurants_sorted = sorted(restaurants)

# Sort cooking times from fastest to slowest
cooking_times_sorted = sorted(cooking_times)

# Expected output--
# Restaurants (A-Z): ['Burger Hub', 'Pizza Palace', 'Sushi Central', 'Taco Town']
# Cooking times (ascending): [12, 25, 28, 29, 30, 31, 32, 35, 40, 55]
print("Restaurants (A-Z):", restaurants_sorted)
print("Cooking times (ascending):", cooking_times_sorted)

print("\n")


# ==============================================================================
# MODULES
# ==============================================================================
# * module = a file containing Python code that can be imported and reused 
#   across programs 
#       * attributes - values 
#       * functions() - predefined operations that each perform a specific task
# * Python contains around 200 built-in modules
#       * os: --> interactions with operating system 
#       * string: --> text processing 
# * import module_name --> imports module 
# * To know what functions a module has, check the documentation OR 
#   help(module_name)

# * os module: 
#       * os.environ --> dictionary containing values abt current environment
#       * os.getcwd() --> returns path of current working directory
#       * os.chdir(path) --> changes current working directory 
# * string module: 
#       * string.ascii_lowercase --> all lowercase letters from a-z
#       * string.digits --> all digits 0-9
#       * string.punctuation --> all special characters 

# ------Examples: Modules------
print("------Examples: Modules------")

# os module--
# Import the os module
import os
# Get the current working directory
print("Current working directory:", os.getcwd())
# Check the environment variables
print("Environment variables:", os.environ)

# string module--
# Import the string module
import string
# Print all ASCII lowercase characters
print(string.ascii_lowercase)
# Print all punctuation
print(string.punctuation)

print("\n")

# ==============================================================================
# PACKAGES
# ==============================================================================
# * package = a collection of modules [that is not built-in, has to be 
#   downloaded before use]
#       * AKA library 
#       *  downloadable from PyPI (directory of packages)
# * How to install a package: 
#       * Open terminal/command prompt
#       * python3 -m pip install package_name
#           * python3 --> executes Python code from terminal 
#           * pip --> preferred installer program, tool used to install packages
#           * ALEX NOTE: for me, I did: py -m pip install package_name
# * To use a package once installed, import as normal: import package_name 
#       * import package_name as pkg --> use alias to refer to package  

# * pandas = a package for data manipulation and analysis 
# * Convention: import pandas as pd 
# * DataFrame = a pandas data type, like a table, for containing large datasets 
#   (better than dictionaries for this)
# * Functions: (**usage: pd.function_name())
#       * DataFrame(my_dict) --> outputs dictionary data as a table
#       * read_csv("file.csv") --> reads CSV file in as a DataFrame
# * DataFrame methods: 
#       * my_dataframe.head() --> displays first five rows of dataframe
#       * my_dataframe.info() --> outputs overview dataframe values, columns, 
#         etc

# * Functions vs. methods: 
#       * function = code that performs a task
#       * method = a function that is specific to a data type 
#           (e.g. dataframe.head())

# ------Examples: Working with the pandas package------
print("------Examples: Working with the pandas package------")
# a dictionary containing information about recent transactions
sales = {'user_id': ['KM37', 'PR19', 'YU88', 'JB18', 'LP65', 'HJ11', 'PR19', 'IJ54'], 
         'date': ['01/05/2025', '01/05/2025', '01/06/2025', '01/06/2025', '01/06/2025', '01/06/2025', '01/07/2025', '01/07/2025'], 
         'order_value': [197.75, 208.21, 134.99, 317.81, 201.3, 157.87, 99.99, 124.5]}

# Import pandas as pd 
import pandas as pd 

# Convert sales to a pandas DataFrame
sales_df = pd.DataFrame(sales)

# Preview the first few rows of our new DataFrame 
print(sales_df.head())
print("\n")

# Given a sales.csv file with user IDs, dates, and order values (costs), read in
# the CSV file as a DataFrame and display info about it 
sales_df = pd.read_csv("Intermediate Python for Developers\sales.csv")
print("--- DataFrame Info ---")
print(sales_df.info())