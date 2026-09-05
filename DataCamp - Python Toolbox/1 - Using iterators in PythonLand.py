# Using Iterators in PythonLand 

def print_separator():
    print("\n--------------------\n")

# ==============================================================================
# INTRODUCTION: ITERATORS AND ITERABLES 
# ==============================================================================
# * iterable = any object that can be looped through (list, str, dict, file 
#   connections, etc.)
#    * = any object with an associated iter() method
# * iterator = an object with a next() method that produces consecutive values
# * applying iter() to an iterable creates an ITERATOR
#    * this is how a for loop works: it takes an iterable, creates an iterator
#      object for it, and then iterates over it 
#    * syntax: 
#       my_iterable = "data to iterate through"
#       my_iterator = iter(my_iterable)
#       next(my_iterator) 
# * next(my_iterator) --> returns next value in iterable until StopIteration
#   error occurs once it has reached the end 
# * *my_iterator --> "splat" or "star" operator `*`: iterates through ALL 
#   elements of the attached iterable at once, in order 
#    * once iterator reaches the end, you must define it again to reset it to 
#      the beginning
# * To iterate over dictionaries: "unpack" the dictionary first;
#   my_dict.items() <-- returns an iterable version 
#   * for key, value in my_dict.items(): 
# * To iterate over a file connection: 
#   file.open("file.txt") 
#   it = iter(file)
#   print(next(it)) <-- prints the next line 
# * a note on the range() function-- you can use range(n) in for loops as if it
#   were a list, but range(n) does NOT create a list of numbers 1-n!! 
#   range(n) creates a range object [technically still an iterable] with an 
#   iterator, which produces values sequentially until it reaches n 
# * Some functions take iterators and iterables as arguments:
#   * list(my_iterable) --> turns iterable into a list 
#   * sum(my_iterable) --> returns a sum of all elements 

# ------Examples: Introduction to Iter[ators|ables]------

# This is an iterable 
flash1 = ["jay garrick", "barry allen", "wally west"]
print("This is an iterable:\n", flash1, "\n")

# This is an iterator
flash2 = iter(flash1) 
print("This is an iterator:\n", flash2)
print(next(flash2))

print_separator()

# Given a list of strings assigned to a variable called "flash":
# - Print each item in the list using a for loop
# - Create an iterator for flash; assign it to a variable called "superhero"
# - Print each item from the iterator by using next() four times 
flash = ["jay garrick", "barry allen", "wally west", "bart allen"]

# print each item in list with for loop 
for item in flash:
    print(item)
print("\n")

# create an iterator for our list 
superhero = iter(flash)

# print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))

print_separator()

# Demonstrating that calling range(n) does NOT pre-create a list of numbers 1-n
# before iterating over it--

# Create an iterator object, small_value, over range(3)
small_value = iter(range(3))
# Print all values in small value (remember: once iterator reaches end, it does
# NOT reset!)
print(next(small_value))
print(next(small_value))
print(next(small_value))
print("\n")

# Loop over range(3) and print the values 
for i in range(3):
    print(i) 
print("\n")

# Now, create an iterator object, googol, over range(10 ** 100)
# IF RANGE CREATED A LIST, THIS WOULD NOT WORK-- a list with this many elements
# would be too big for computer memory to hold 
googol = iter(range(10 ** 100))

# print the first 5 values from googol to prove the computer can handle an
# iterator, though, not a pre-generated list with 10*100 items
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print("\n")

print_separator()

# Iterators as function arguments-- 

# Create a range object that would produce values 10-20
values = range(10, 21)
print(values)

# Create a list of values 10-20
values_list = list(range(10, 21))
print(values_list) 

# Use sum() to get the some of all values from the range object `values`
values_sum = sum(range(10, 21))
print(values_sum)

print_separator()

# ==============================================================================
# FUNCTIONS TO USE WITH ITERABLES
# ==============================================================================
# * enumerate(my_iterable, start=0): takes any iterable and an optional index to 
#   start at, returns an "enumerate object" containing a sequence of pairs of 
#   each value + their index
#   * Ways to "unpack" (print to screen): 
#      * list(my_enumerate) --> convert enumerate object into a list of tuples
#        that can be printed 
#      * for index, value in enumerate(my_iterable):
#        print(index, value) --> see all element-index pairs printed out 
# * zip(*arg_iterables): takes any number of iterables, returns a "zip object" 
#   (an iterator of tuples), where each tuple contains the nth element of each 
#   iterable grouped together
#   * Ways to unpack:
#      * list(my_zip)
#      * for z1, z2, etc in my_zip:
#           print(z1, z2, etc)
#      * my_zip = zip(list1, list2)
#        print(*my_zip)
# * *my_iterable: "splat operator" `*` --> unpacks an iterable into positional 
#   arguments in a function call 
#    * e.g. print(*my_iterable) == print(element1, element2, element3, ...) 
#    * warning: will iterate to end, need to re-define to reset iterator

# ------Examples: Functions to use with iterables------

# Practice with enumerate()-- 
# Given a list of strings, turn it into an enumerate object. Then turn this
# object into a list and print it out. 
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']
mutant_list = list(enumerate(mutants))
print(mutant_list, "\n")

# Unpack and print the tuples generated by calling enumerate() on mutants.
for index1, value1 in enumerate(mutants): 
    print(index1, value1)
print("\n")

# Change start index to 1 
for index2, value2 in enumerate(mutants, start=1): 
    print(index2, value2)

print_separator()

# Practice using zip()--
# Given three lists of strings: 
# - Create a list of tuples where the nth tuple in this list contains all 
#   elements at index n of the three original string lists. Print it. 
# - Create a zip object using the three lists. Print it. 
# - Unpack the zip object and print the tuple values. 
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']
aliases = ['prof x', 
           'iceman', 
           'nightcrawler', 
           'magneto', 
           'shadowcat']
powers = ['telepathy', 
          'thermokinesis', 
          'teleportation', 
          'magnetokinesis', 
          'intangibility']

# Create a list of tuples and print the list 
mutant_data = list(zip(mutants, aliases, powers))
print(mutant_data, "\n")

# Create a zip object from the three lists and print it 
mutant_zip = zip(mutants, aliases, powers)
print(mutant_zip, "\n")

# Unpack the zip object and print all the tuple values 
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)

print_separator()

# Using * and zip to "unzip" tuples--
# Given two tuples:
# - Create a zip object to zip these two tuples together 
# - Print the resulting tuples using * to unpack them into positional arguments
#   for the print() function
# - Recreate the zip object, then unzip into separate tuples using * and zip()
# - Check if unpacked tuples are equivalent to the original tuples 
mutants = ('charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pryde')
powers = ('telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility')

# Zip mutants and powers together 
z1 = zip(mutants, powers)

# Print the resulting tuples
# will print: (mutant0, power0), (mutant1, power1), ...
print(*z1)

# Create the zip object again (needed to reset after using *), then unzip
z1 = zip(mutants, powers)
# input --> zip((mutant0, power0), (mutant1, power1), ...)
# output --> result1 = (mutant0, mutant1, ...), result2 = (power0, power1, ...) 
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to the original tuples
print(result1 == mutants)
print(result2 == powers)

print_separator()

# ==============================================================================
# USING ITERATORS TO LOAD LARGE FILES INTO MEMORY 
# ==============================================================================
# * If you want to process data, but there is too much to hold in memory,
#   load it in chunks: 
#    1.) Load one chunk of data 
#    2.) Perform desired operation(s) on chunk
#    3.) Store the result
#    4.) Discard the chunk
#    5.) Load in the next chunk
# * Use pandas package to do this: 
#    * read_csv(file_name, chunksize=n): loads file in chunks of n lines at a 
#      time
#    * Usage example (loading in a csv with one column containing numbers): 
#      import pandas as pd
#      total = 0 
#      for chunk in pd.read_csv("data.csv", chunksize=1000):
#         total += sum(chunk["column_name"])

# ------Examples: Functions to use with iterables------

# Given a tweets.csv file in this directory, which contains tweets from 
# Twitter: 
# - Initialise an empty dictionary, counts_dict. In this dictionary, key = the 
#   language a tweet is in, and value = the count of tweets in that language. 
# - Load the file in, chunk-by-chunk, with a chunk size of 10 
# - For each chunk, iterate over the column "lang" (which represents the 
#   language that a tweet is in) and increment the count of tweets in each 
#   tweet's language in count_dict. 

# BY THE WAY-- FUN ALEX NOTE: 
# to get the tweets.csv file that DataCamp has preloaded into their environment,
# I did the following: 
# df = pd.read_csv("tweets.csv") <-- creates dataframe with CSV data
# print(df.to_csv()) <-- converts dataframe to CSV string, prints the result
# copied and pasted string from terminal into new file in this directory

import pandas as pd 

# Initialise an empty dictionary: counts_dict
counts_dict = {}

# Iterate over the file chunk by chunk
# read_csv() creates a dataframe, so we are iterating through each chunk of 10
# rows at a time 
for chunk in pd.read_csv("tweets.csv", chunksize=10):
    
    # Iterate over each value in the "lang" column of this chunk 
    for entry in chunk["lang"]:
        # if we have already added this language to dictionary, simply
        # increment its count
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            # create new entry for this language
            counts_dict[entry] = 1

# Print the populated dictionary
# ALEX NOTE: to be explicit, this shows how many tweets were in each language 
print(counts_dict)

print_separator()

# - Define a function count_entries(), which has 3 parameters: csv_file
#   (the file name), c_size (chunk size), and colname (column name). 
# - Put the script written above for counting entries in a column into this 
#   function. 
# - Then, use this function to do the same task as in the last example-- 
#   counting the number of tweets in each language from tweets.csv with a chunk
#   size of 10. 

# Define function that counts entries
def count_entries(csv_file, c_size, colname): 
    """
    Return a dictionary with counts of occurrences as value for each key.
    """ 

    # Initialise an empty dictionary for holding results 
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):
        
        # Iterate over each value in the given column 
        for entry in chunk[colname]:
            # increment count of value in dictionary 
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                # create new entry for this language
                counts_dict[entry] = 1

    return counts_dict

# Use count_entries() to count the number of tweets in each language from 
# tweets.csv, with a chunk size of 10
result_counts = count_entries("tweets.csv", 10, "lang")
print(result_counts)

print_separator()