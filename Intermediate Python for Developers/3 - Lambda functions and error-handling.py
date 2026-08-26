# Lambda functions and error-handling
# Example used in this lesson: [project theme, e.g. recipe scaler] 

def print_separator():
    print("\n--------------------\n")

# ==============================================================================
# LAMBDA FUNCTIONS  
# ==============================================================================
# * lambda function = an "anonymous function"-- doesn't require a name
# * Useful for: doing something only once, or doing something simple 
# * To use: (lambda x, y, z: expression_here_using_xyz)(value1, value2, value3)
#    * Convention: if only a single argument, call it "x" 
# * To store as a variable: 
#   my_lf = lambda x: function_body_here
#    * To call: my_lf(arguments_here)
# * How to use lambda functions with iterables:
#    * my_results = map(my_lambda_function, iterable_value) --> applies function 
#      to all elements in an iterable
#    * may need to convert my_results to a datatype to view, e.g. 
#      list(my_results)

# ------Examples: Lambda Functions------

# Given a file's base size and how much storage will be needed to store extra 
# file information (given as a percentage of base file size), create a lambda 
# function that calculates the total file size.  
file_size = 2500
extra_space = 0.15 # ALEX NOTE: regard this as a constant. What is the 
                    # convention for constants in Python anyway? All caps?
                    # PEP 8 says all caps separated by underscores. 
                    # https://peps.python.org/pep-0008/#constants 
                    # DataCamp had it as lowercase but just FYI 

# Define a lambda function
calculate_total = lambda x: x * (1 + extra_space)

# Call the lambda function
# Expected output: 2875
print(calculate_total(file_size))

# Define and call the above lambda function in one line
# Expected output: 2875
print((lambda x: x * (1 + extra_space))(file_size))

# Using lambda functions on iterables--
# Given a list of colleagues' names, change all colleagues' names to lowercase
# and replace all spaces with underlines. 
# Use a lambda function for this.  
# Then convert the resulting map object to a list and print the result. 
colleagues = ["Sarah Martinez", "Michael Chen", "Emily Brown"]

# Apply the lambda function to each colleague's name
cleaned = map(lambda x: x.replace(" ", "_").lower(), colleagues)

# Convert map object to list 
cleaned_list = list(cleaned)
# Expected output: ['sarah_martinez', 'michael_chen', 'emily_brown']
print(cleaned_list)

print_separator()

# ==============================================================================
# INTRODUCTION TO ERRORS 
# ==============================================================================
# * error == exception 
#   * TypeError = you used an incompatible data type for a task 
#   * ValueError = the value you provided was not within an acceptable range
# * traceback = information about the type of information that occurred
#   * Look for: *your* file location & code, the line number of the error
# * source code = the code in packages that other people made

# ------Examples: Errors------

# Can you fix the errors in this code? 
# (solution: missing comma in list, use wrong variable name)
# sales = [125.97, 84.32, 99.78 154.21, 78.50, 83.67, 111.13]
# print(sale)

# How can you fix the error below? 
# (solution: remove "content=True" because that keyword does not exist in get())
# import requests
# requests.get(url="https://app.datacamp.com", content=True)

print_separator()

# ==============================================================================
# ERROR HANDLING 
# ==============================================================================
# * When writing a function, consider:
#   * Where might other developers go wrong when using your code?
#   * How will they want to use it? 
# * Ways to proactively prevent errors:
#   * control flow (if, elif, else)
#   * docstrings 
# * Ways to handle errors when they occur & help others debug: 
#   * try-except keywords-- 
#       def my_funct(): 
#           try:
#               code that might cause an error here
#           except: 
#           code to do if an error occurs (e.g. print error message)
#       * program will not terminate
#       * good for non-sequential scripts 
#   * raise keyword --> tells Python to raise an Exception--
#       def my_funct():
#           if some_condition_to_avoid_errors
#               do_stuff
#           else
#               raise TypeOfError("error message here")
#       * stops program execution
#       * use to prevent further execution that may produce unwanted results

# ------Examples: Errors------

# Define a function clean_text() that tries to clean a string by replacing
# spaces with underscores and converting all text to lowercase. If the parameter
# passed to this function is not a string, print a helpful message instead. 

def clean_text(text):
    try:
        return text.replace(" ", "_").lower()
    except: 
        print("The clean_text() function expects a string as an argument, please check the data type provided!")

# Expected output: "The clean_text() function expects a string as an argument,
# please check the data type provided!"
clean_text(187)

# Revise the above clean_text() function to raise an error if an incorrect 
# data type is used. 
def clean_text(text):
    if type(text) == str:
        return text.replace(" ", "_").lower()
    else:
        raise TypeError("The clean_text() function expects a string as an argument, please check the data type provided!")

# Expected output: user_name_187
print(clean_text("User Name 187"))