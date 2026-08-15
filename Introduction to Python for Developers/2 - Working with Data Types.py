# Working with Data Types
# Example used in this lesson: recipe scaler 

# * method = a function that is only available to a specific data type 
#    * var_name.method_name()

# STRINGS:
# * Declaring: 
#    * 'single quotes' or "double quotes" both valid
#    * """multi-line string
#      uses triple quotes"""
# * Methods: 
#    * .replace(a, b) --> finds and replaces all instances of a with b
#    * .lower() --> to lowercase 
#    * .upper() --> to uppercase 

# ---Strings---
pasta_type = "pasta" 
ingredient_one = "BASIL" 

# Store multi-line cooking instructions 
cooking_instructions = """Step 1: Boil water in a large pot
Step 2: Add pasta and cook for 10 minutes
Step 3: Drain and serve with sauce""" 

# Update pasta type to be more specific with .replace() method 
pasta_type = pasta_type.replace("pasta", "fusilli pasta")

# Convert ingredient_one to lowercase 
ingredient_one = ingredient_one.lower() 

# Expected output:
# fusilli pasta
# basil
print(pasta_type)  
print(ingredient_one) 

# LISTS: 
# * store any combination of data types together 
# * Declaring: my_list = [a, b, c] 
# * Accessing: (zero-based index) 
#    * my_list[index]
#    * my_list[-1] --> returns final element 
#    * my_list[a:b] --> returns all elements where a <= index < b  
#       * a:b = "slice syntax" 
#       * my_list[a:] --> returns all elements from index a to the end 
#       * my_list[:b] --> returns all elements from beginning up to but not
#         including index b 
#    * my_list[::n] --> returns every nth element ("step values") 
#       * my_list[::2] --> every 2nd element 
#    * my_list[i::n] --> every nth element starting at index i 
#       * my_list[1::3] --> every 3rd element starting at index 1 

# ---Lists--- 
# Create a list of ingredients --> shopping list 
ingredients = ["fusilli", "tomatoes", "garlic", "basil", "olive oil", "salt"] 

# Create a list of ingredient quantities in grams 
quantities = [500, 400, 15, 20, 30, 10] 

print(ingredients)
print(quantities)

# Create quick previews of shopping list-- 

# Get the second ingredient for your preview 
second_ingredient = ingredients[1] 

# Get the last item in quantities 
last_quantity = quantities[-1]

# Get every other ingredient starting from the first 
alternate_ingredient = ingredients[::2] 

# DICTIONARIES
# = key-value pairs 
# * Declaring: my_dict = {"key1": value1, 
#                         "key2": value2}
# * Accessing: 
#    * my_dict["key1"] --> returns value1
#    * my_dict.values() --> returns list of all values 
#    * my_dict.keys() --> returns list of all keys 
#    * my_dict.items() --> returns list of all key-value pairs 
#       * each key-value pair stored as a tuple  
# * Adding or modifying a key-value pair: my_dict["key"] = value 

# ---Dictionaries--- 

# Create a recipe dictionary
# (key: ingredient, value: quantity in grams)
recipe = {"olive_oil": 30,
          "garlic": 15, 
          "tomatoes": 400}

# Add basil to the recipe dictionary 
recipe["basil"] = 20

print(recipe)

# Get all ingredient names 
ingredient_names = recipe.keys() 

# Get all quantities 
quantities = recipe.values() 

# Get all key-value pairs 
recipe_items = recipe.items() 

print("Ingredient names:", ingredient_names)
print("Quantities:", quantities)
print("Recipe items:", recipe_items)

# SETS:
# * contains multiple, unordered, unique values only --> good for de-duplicating 
#   data sets 
#    * values can be added or deleted, but not modified 
#    * searching is much faster than other data types (e.g. lists)
# * Declaring: my_set = {val1, val2, ...}
# * casting = converting one data type to another 
#    * set(my_list) --> converts existing variable to a set 
# * sorted(my_set) --> returns list of values in alphabetical order 

# TUPLES: 
# * immutable, ordered group of values-- cannot add, remove, or change values
# * Declaring: my_tuple = (val1, val2, ...)
# * Casting: tuple(my_list) --> converts to a tuple 
# * Accessing: my_tuple[index]

# ---Sets and Tuples---
# Store the conversion between cup and milliliter as a tuple 
cup_conversion = (1, 240)

# Check the data type of cup_conversion 
print(type(cup_conversion))

# Pretend you've been collecting a list of all ingredients needed across 
# multiple recipes you want to make 
all_ingredients = ["fusilli pasta", "tomato", "cheese", "salt", "pepper", 
                   "eggs", "pepper", "green onion", "salt"]

# Convert ingredient list to a set in order to see what *unique* ingredients
# you need to buy (i.e. de-duplicate the list of ingredients) 
unique_ingredients = set(all_ingredients)

# Print items in alphabetical order 
print(sorted(unique_ingredients))