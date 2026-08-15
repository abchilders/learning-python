# Control flow and loops
# Example used in this lesson: recipe scaler 

# OPERATORS: (the same as usual tbh)
# * == equality
# * != inequality 
# * <, <=, >, >= comparison 

# IF/ELSE STATEMENTS: 
# if some_condition:
#    action here 
# elif other_condition:
#    action here 
# else: 
#    action here  

# ---If/Else Statements---
# Pretend you've got a tomato and basil pasta recipe. You have a list of
# ingredients needed for this recipe. Before scaling up the recipe, you want to 
# ensure you have enough of each ingredient already. 
# key = ingredient name, value = quantity in grams 
ingredients_needed = {'fusilli': 1000, 'tomatoes': 800, 'basil': 40, 
                      'garlic': 30, 'olive oil': 30, 'salt': 15}
pantry_stock = {'tomatoes': 500, 'basil': 80, 'fusilli': 1000, 'garlic': 12}

# If you have enough tomatoes for the party, print a confirmation message.
# If you don't, but you do have at least 800 grams of tomatoes for a smaller 
# party, print a message indicating so. 
# Otherwise, print a message indicating you need to buy tomatoes. 

# Check if you have enough tomatoes for the full party 
if pantry_stock["tomatoes"] >= ingredients_needed["tomatoes"]: 
    print("Enough tomatoes for the party!")

# If not, check if you have enough for a smaller gathering 
elif pantry_stock["tomatoes"] >= 800:
    print("Only enough tomatoes for a small gathering.")

# If not, then you need to buy more tomatoes 
else: 
    print("Need to buy tomatoes before the party.")

# Check if you have exactly the right amount of basil needed, or if you need to
# adjust your shopping list
required_basil = ingredients_needed["basil"]
basil_grams = pantry_stock["basil"]

if basil_grams == required_basil:
    print("Perfect! You have exactly the right amount of basil.")
else: 
    print("You need to adjust your basil quantity.")

# FOR LOOPS: 
# * for value in sequence: 
#      action here
#    * value = "iterator"
#    * sequence = "iterable" (list, strings, etc.)
#       * range(a, b): generates list of numbers from a up to b (but not 
#         including b)
#       * if iterable is a string: this will iterate through each character
# * for key, value in my_dict.items(): --> .items() returns tuples (key-value 
#   pairs), so you need to provide two iterators, one for each position in tuple

# ---For Loops---
ingredients = ingredients_needed.keys() 

# Loop through each ingredient in your list and print 
for item in ingredients: 
    print(item) 

# Create for loop that prints numbers 1 to 6 
for item in range(1, 7): 
    print("Adding ingredient", item)

# Categorise ingredient quantities into large (400g+), medium(200g+), and small
# (anything less than 200g) 
quantities = [500, 400, 20, 15, 15, 7]
for qty in quantities: 
    if qty >= 400:
        print("Large quantity")
    elif qty >= 200:
        print("Medium quantity")
    else:
        print("Small quantity")

# Given a dictionary with key-value pairs representing ingredients and their 
# quantities in a recipe, double the recipe by printing each ingredient's 
# quantity scaled up by a factor of 2
recipe = {
    "fusilli": 500,
    "tomatoes": 400, 
    "basil": 20, 
    "garlic": 15, 
    "olive oil": 15, 
    "salt": 7
} 

# Loop through recipe dictionary items
for ingredient, qty in recipe.items():
    # Calculate the scaled quantity by multiplying by 2 
    scaled_qty = qty * 2
    print(ingredient, ":", scaled_qty, "g")

# WHILE LOOPS: 
# * while some_condition: 
#      action here
# * P.S.-- Ways to handle infinite loops: 
#    * put "break" into your loop before you run it 
#    * Ctrl + C (Windows) to interrupt program while it's running

# ---While Loops--- 

# Count guest RSVP confirmations using a while loop
# ALEX NOTE: this could also be a for loop if we are incrementing in regular 
# intervals... 
total_confirmations = 10
guest_count = 0 

while guest_count < total_confirmations:
    guest_count += 1
    print(guest_count, "guests so far!")
    print("We have", guest_count, "guests coming!")

# Create a while loop that loops through each ingredient and prints 
# how many ingredients have been looped through so far 
# ALEX NOTE: this could also be a for loop...

# tracks how many ingredients we've verified
ingredients_checked = 0 
# represents total number of ingredients in our tomato and basil pasta recipe
total_ingredients = 7

while ingredients_checked < total_ingredients:
    # Increment the counter
    ingredients_checked += 1
    # Check if less than 4 ingredients reviewed 
    if ingredients_checked < 4: 
        print("More than half remaining")
    # Check if 6 or fewer ingredients reviewed 
    elif ingredients_checked <= 6: 
        print("Nearly finished checking")
    else:
        print("All ingredients verified!")

# BUILDING A WORKFLOW-- other logic keywords:
# * in --> check if a value is in a variable/data structure 
#    * e.g. if "pasta" in recipe.keys(): 
# * and
# * or 
# * not --> negates above keywords 
#    * e.g. if "salt" not in pantry_items
# +=, -=, ... 

# * bonus tidbit: list.append() --> adds item to list 

# ---Building a Workflow---

# Make a shopping list by looping through each ingredient + required amount in 
# recipe, checking our pantry stock to see if we have enough, and then adding to
# shopping list if not 
recipe = {'pasta': 500, 'tomatoes': 400, 'basil': 20, 'garlic': 15, 
          'olive_oil': 30, 'salt': 10}
pantry_stock = {'pasta': 100, 'tomatoes': 1500, 'basil': 20, 'garlic': 10, 
                'olive_oil': 10, 'salt': 150}

# Create an empty shopping list
shopping_list = [] 

# Loop through each ingredient and required quantity 
for ingredient, required_qty in recipe.items():
    # Check if we need more than what we have 
    if required_qty > pantry_stock[ingredient]: 
        # Add the ingredient to our shopping list 
        shopping_list.append(ingredient)

# Display the shopping list 
print("Shopping list:", shopping_list)

# ALEX NOTE: DataCamp also provided this exercise to count how many items we
# have in our shopping list.
# I know that this is for the purpose of practicing for loops. However, I could
# not cease my heart's yearning to simply retrieve the list's length instead. So
# here is DataCamp's solution, and then also my solution. 

# Count how many items to buy
items_to_buy = 0

for item in shopping_list:
    items_to_buy += 1

# Display results
print(shopping_list)
print(items_to_buy)

# Alternatively: 
print("Items to buy:", len(shopping_list))

# ---Putting it all together into a recipe scaler---
# Initialise pantry with quantities of ingredients, recipe with ingredient 
# amounts, and scale factor indicating ratio of number of servings needed to 
# number of servings in original recipe 
pantry = {'pasta': 500, 'tomatoes': 800, 'olive_oil': 100, 'garlic': 15}
recipe = {'pasta': 500, 'tomatoes': 400, 'garlic': 15, 'basil': 20, 
          'olive_oil': 30, 'salt': 10}
scale_factor = 10/4 # equivalent to 2.5 

# Create shopping list for missing items 
shopping_list = []

# Loop through each ingredient and amount in the recipe 
for ingredient, amount in recipe.items(): 
    # Calculate the amount of this ingredient needed for this party, scaled to 
    # scale_factor 
    needed_amount = amount * scale_factor

    # Check if we need to buy this ingredient 
    if ingredient not in pantry.keys() or needed_amount > pantry[ingredient]: 
        shopping_list.append(ingredient)