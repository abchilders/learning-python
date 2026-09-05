# List comprehensions and generators 
# Example used in this lesson: extracting data from time-stamped Twitter data

import pandas as pd

def print_separator():
    print("\n--------------------\n")

# ==============================================================================
# LIST COMPREHENSIONS
# ==============================================================================
# * create lists from other lists, in a single line (no for loop needed) 
# * new_list = [expression_to_output for iterator in old_iterable] 
#   --> alternative to using a for loop to iterate through a whole list/other 
#   iterable  
#    * equivalent to--
#      for item in old_iterable: 
#         new_list.append(expression_using_item)
#    * basically just switch the "for i in my_list" and what goes after it
# * To replace nested for loops with list comprehensions: 
#   list_of_pairs = [(num1, num2) for num1 in iterable1 for num2 in iterable2]
#    * outer loop first, then inner loop 
#
# * Conditionals in comprehensions: 
#    * Filtering the iterable: 
#      new_list = [output_expr for item in my_iterable if some_condition] 
#      --> only adds output to new_list if some_condition is True 
#    * Changing output based on a condition: 
#      new_list = [output_expr1 if some_condition else output_expr2 for my_iterable]
#      --> if condition is True, outputs expr1. else, outputs expr2. 
#       * again, just switch the order of if (condition): smth/else: smth
#
# * Final syntax: [output_expr some_output_condition for item in my_iterable 
#   some_iterable_condition]

# ------Examples: List Comprehensions------

# This for loop and this list comprehension are equivalent: 
nums = [12, 8, 21, 3, 16]

new_nums1 = []
for num in nums:
    new_nums1.append(num+1)
print(new_nums1)

new_nums2 = [num + 1 for num in nums]
print(new_nums2)

print_separator()

# This nested for loop and this list comprehension are equivalent too: 
# they both get all combinations of pairs of numbers where the first number is 
# 0 or 1 and the second number is 6 or 7

pairs_1 = []
for num1 in range(0,2):
    for num2 in range(6, 8):
        pairs_1.append((num1, num2))
print(pairs_1)

pairs_2 = [(num1, num2) for num1 in range(0, 2) for num2 in range(6, 8)]

print_separator()

# Write a list comprehension that produces a list of the squares of numbers 
# ranging from 0 to 9.
squares = [i*i for i in range(0, 10)]

assert(squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])

# Nested list comprehensions--
# Write a list comprehension that outputs the following 5x5 matrix: 
# matrix = [[0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4]]
#
#         generates a list of ints 0-4     does it 5 times
matrix = [[col for col in range(0, 5)] for row in range(0, 5)]

# testing/verification
for row in matrix:
    print(row)

assert(matrix == [[0, 1, 2, 3, 4],
                  [0, 1, 2, 3, 4],
                  [0, 1, 2, 3, 4],
                  [0, 1, 2, 3, 4],
                  [0, 1, 2, 3, 4]])

print_separator()

# Create a list of squares of only even numbers between 0-9.
# Note: x ** y --> Python's version of "x^y" (exponent operator)
#
#          output num squared                   only if num is even
even_squares = [num ** 2 for num in range(0, 10) if num % 2 == 0]

print(even_squares)
assert(even_squares == [0, 4, 16, 36, 64])
print_separator()

# Create a list that, for each integer between 0-9, contains the following: 
# - if the integer is odd, output 0
# - if the integer is even, output the integer squared 
even_squares_padded = [num ** 2 if num % 2 == 0 else 0 for num in range(0, 10)]

print(even_squares_padded)
assert(even_squares_padded == [0, 0, 4, 0, 16, 0, 36, 0, 64, 0])
print_separator()

# Given a list of strings, create a list that only includes the strings that
# have 7 characters or more. 
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

new_fellowship = [member for member in fellowship if len(member) >= 7]

print(new_fellowship)
assert(new_fellowship == ['samwise', 'aragorn', 'legolas', 'boromir'])
print_separator()

# Given the same list of strings (fellowship), create a list that keeps members
# of fellowship with 7 or more characters, but replaces others with an empty 
# string. 
new_fellowship = [member if len(member) >=7 else "" for member in fellowship]

print(new_fellowship)
assert(new_fellowship == ['', 'samwise', '', 'aragorn', 'legolas', 'boromir', '']) 
print_separator()

# ==============================================================================
# DICTIONARY COMPREHENSIONS
# ==============================================================================
# * create dictionaries by iterating over some iterable in a single line of code
# * my_dict = {key: value for iterator in my_iterable}

# ------Examples: Dictionary Comprehensions------

# Create a dictionary where the keys are all integers 0-8, and their respective
# values are the corresponding negative integers.
pos_neg = {num: -num for num in range(0, 9)}

print(pos_neg)
assert(pos_neg == {0: 0, 
                   1: -1, 
                   2: -2, 
                   3: -3, 
                   4: -4, 
                   5: -5, 
                   6: -6, 
                   7: -7, 
                   8: -8})
print_separator()

# Given a list of strings, create a dictionary comprehension where the key is a
# string in the given list, and the value is the length of that string. 
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

new_fellowship = {member: len(member) for member in fellowship}

print(new_fellowship)
assert(new_fellowship == {"frodo": 5, 
                          "samwise": 7, 
                          "merry": 5, 
                          "aragorn": 7, 
                          "legolas": 7, 
                          "boromir": 7, 
                          "gimli": 5})
print_separator()

# Printing a list of the creation times of all tweets in a dataset-- 
# Import tweets.csv as a dataframe. 
# Extract the column 'created_at' from the dataframe and assign the result to 
# tweet_time. (this extracted column will be a Series data structure, a single-
# dimension array)
# Create a list comprehension that extracts only the time from each created-at
# timestamp (format example: Tue Mar 29 23:40:18 +0000 2016)
# Then print all extracted times. 

# import tweets.csv
df = pd.read_csv("tweets.csv")

# extract the "created_at" column as a Series of timestamps
tweet_time = df["created_at"]

# create list comprehension that extracts only the time from each timestamp
tweet_clock_time = [entry[11:19] for entry in tweet_time]

# print all extracted created-at clock times
print(tweet_clock_time)

print_separator()

# Do the same as above, BUT only select and print clock times that end in 19 
# (i.e. tweets that were created at 19 seconds after the minute).
# Expected output: a list of times ending in 19 only
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == "19"]
print(tweet_clock_time)

print_separator()

# ==============================================================================
# GENERATOR EXPRESSIONS
# ==============================================================================
# * like a list comprehension, but returns an iterable "generator object" 
#   instead of a list 
#    * like "lazy evaluation" where each item is only evaluated when you need it
#    * generates sequences on the fly --> saves memory (good for large lists)
#    * dict.items() and range() also use generators, FYI
# * my_generator = (expression_to_output for iterator in old_iterable)
# * list(my_generator) --> converts generator to a list stored in memory
# * next(my_generator) --> iterates to next item in my_generator
#
# * Conditional expressions: work the same as in a list comprehension
#    * To filter the iterable: 
#      (output_expr for iter in my_iterable if some_condition)
#
# * Generator functions: create generator objects, which can be iterated over to 
#   to "yield" a sequence of values rather than "return"ing just one single 
#   value 
# * def my_generator_function(n): 
#      i = 0
#      while i < n: 
#         yield some_value_to_output
#         i += 1
# * To print output of a generator function: 
#   result = my_generator_function()
#   for item in result: 
#       print(item)

# ------Examples: GENERATOR EXPRESSIONS------

# DO NOT UNCOMMENT THIS UNLESS YOU WANT TO CRASH YOUR COMPUTER. ALEX. 
# This is an example of something that you'd want to replace *with* a generator
# to avoid a crash from creating something way too big to be stored in memory. 
# [num for num in range(10**1000000)] --> list is 10^1,000,000 items long 

# YOU *CAN* DO THIS INSTEAD AND AVOID CRASHING YOUR COMPUTER! 
# BUT DO NOT UNCOMMENT UNLESS YOU WANT A MASSIVE LIST ON YOUR SCREEN!
# (num for num in range(10*1000000))

# Create a generator function that generates values from 0 to n. 
def num_sequence(n): 
    """Generate values from 0 to n."""
    i = 0 
    while i < n: 
        yield i 
        i += 1

# Test: use num_sequence() to produce a sequence of integers 0-4 
result = num_sequence(5)

# num_sequences() returns a generator object that will iterate over the values
print(type(result))
for item in result: 
    print(item) 

print_separator()

# Create a generator object that will produce values from 0 to 30. 
# Print the first 5 values by using next(). Then print the rest of the values by 
# using a for loop to iterate over the generator object. 

# create generator object producing values 0-30
result = (num for num in range(0, 31))

# print the first 5 values using next() 
# Expected output: 0 1 2 3 4 (separated by newlines)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# print the remaining values using a for loop
for value in result:
    print(value) 

print_separator()

# Given a list of strings, write a generator expression that will generate the
# lengths of each string in the list.
# Then iterate over the generator to print each value (representing string 
# length).
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# create generator object
lengths = (len(person) for person in lannister)

# print all string lengths 
# Expected output: 6 5 5 6 7 (separated by newlines)
for value in lengths:
    print(value)

print_separator()

# Create a generator function, get_lengths(), that does the same thing as the 
# generator expression (len(person) for person in lannister) above-- given a 
# list, it should yield the length of each string in the list. 
# Then print the values generated by get_lengths(). 
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# define generator function
def get_lengths(input_list):
    """Generator function that yields the length of the strings in input_list.
    """
    for person in input_list:
        yield len(person)

# print all values generated by get_lengths()
# expected output: 6 5 5 6 7 (separated by newlines)
for value in get_lengths(lannister):
    print(value)

