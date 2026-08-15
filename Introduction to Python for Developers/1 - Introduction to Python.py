# Introduction to Python 
# Example used in this lesson: recipe scaler 

# STANDARD DEVELOPMENT PRACTICES:
# * Start small 
# * Iterate
# * Test as we build - print("message here")
# * Document - comments with # 

# Your first print functions
print("Hello, world!")
print("Welcome to the recipe scaler")

# VARIABLES AND DATA TYPES: 
# * Declare or modify a variable --> var_name = value
#    * Convention: use lowercase and underscores 
# * Python assigns data types automatically
#    * Strings: 'value' or "value" 
#       * recommend using "" so that strings can contain apostrophes 
#    * Integers
#    * Floats: numbers with decimals (no double???) 
#    * Boolean: True, False
# * type(var_name): returns data type of variable
# * Arithmetic operators: +, -, *, /
#    * with strings: + = concatenation, * = duplicate (e.g. "Hi"*3 == "HiHiHi") 

# ---Declaring variables---
# Store the pasta type as a string
pasta_type = "Spaghetti"
# Store the quantity as an integer
quantity = 80

# Print the pasta type
print(pasta_type)
# Print the quantity
print(quantity)

# ---Modifying variables---
# Update the pasta type to fusilli
pasta_type = "fusilli"
# Update the quantity to 100
quantity = 100
print(pasta_type)
print(quantity)

# ---Numeric data types---
# Store the number of garlic cloves as an integer
garlic_cloves = 3

# Store the olive oil amount as a float
olive_oil_tbsp = 2.5
print(olive_oil_tbsp)

# Increase the olive oil amount
new_olive_oil_tbsp = 2.5 + 1

print(garlic_cloves)
print(new_olive_oil_tbsp)

# ---Boolean data type---
# Track if you have pasta at home
has_pasta = True
# Track if you have garlic
has_garlic = False

print(has_pasta)
print(has_garlic)

# ---checking a variable's data type---
# Check the data type of olive_oil_tbsp
print(type(olive_oil_tbsp))
# Check the data type of has_pasta
print(type(has_pasta))