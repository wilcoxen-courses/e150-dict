#! /bin/python3
#  Jan 20 (PJW)

import json 

#  Create a couple of simple dictionaries

co = {'name':'Colorado', 'capital':'Denver'}
ny = {'name':'New York', 'capital':'Albany'}

print('\nThis is the original NY dictionary:')
print(ny)

#  Add some additional information to each dictionary: the
#  state's postal code

co['po'] = 'CO'
ny['po'] = 'NY'

print('\nThis is the revised NY dictionary:')
print(ny)

#  Look up the value at a dictionary key and print it out

name = ny['name']
capital = ny['capital']

print("\nThe capital of",name,"is",capital)

#  Make a couple of lists of dictionaries in different ways.
#  Start with a simple one.

list1 = [co,ny]

print('\nHere is list1:')
print(list1)

print('\nHere is list1 with better formatting:')
print( json.dumps(list1,indent=4) )

#  Now build a longer list by staring with the first two states
#  and then extracting additional state information from a 
#  list of strings. The strings have extra spaces and use 
#  semicolons as separators to show how that kind of data
#  can be parsed.

list2 = [co,ny]

others = [
    "  Massachusetts ; Boston     ; MA  ",
    "     California ; Sacramento ; CA  ",
    "          Texas ; Austin     ; TX  "
    ]

#  Work through the list of strings one at a time

for line in others:

    #  Removes leading and trailing space from the line. Not strictly
    #  needed here but important when reading from a file and not 
    #  splitting on blank space.
    
    line = line.strip()  
    
    #  Now split the line on the semicolons
    
    words = line.split(';')
    
    #  Go through the list of words and remove any extra spaces
    #  around them, making a new list in the process
    
    clean_words = []
    for word in words:
        clean_words.append( word.strip() )
    
    #  Here's a more elegant way to do the same thing using a
    #  list comprehension, which is a compact way to build a new
    #  list out of an old one:
        
    clean2_words = [word.strip() for word in words]

    #  Now pull out the parts and make a new dictionary
        
    name    = clean2_words[0]
    capital = clean2_words[1]
    po      = clean2_words[2]
    
    new_dict = {'name':name, 'capital':capital, 'po':po}
    
    #  Append the new dictionary to the list
    
    list2.append(new_dict)

#  Print out the longer list
    
print('\nHere is list2:')
print(list2)

#  Now go through list2 and show all the capitals

print("\nState capitals:")

for state in list2:
    name = state['name']
    capital = state['capital']
    print("   ",name,"->",capital)
    
#  Digression: example using round()

numer = 20.0
denom = 3.0
ratio = numer/denom
rounded = round(ratio,2)

print('\n20/3 unrounded:',ratio)
print('20/3 rounded to 2 decimal places:',rounded)

#  Digression: looping through the letters of a string

print("\nLooping through a string:")

for letter in "python":
    print(letter)

#  Now make a dictionary of the dictionaries, which will be very 
#  convenient for looking things up by state name. Use each state's name
#  as the key and each state's individual dictionary as the value.
    
super_dict = {}
for state in list2:
    name = state['name']
    super_dict[name] = state 
    
print('\nHere is super_dict:')
print( json.dumps(super_dict,indent=4) )

#  Use that to list the state capitals with the states in 
#  alphabetical order. 

print("\nState capitals with states in alphabetical order:")
    
#  First, get the state names, since they are the keys to the 
#  super_dict dictionary. Then go through them in alphabetical 
#  order. For each name, the value in the dictionary will be 
#  the dictionary for the individual state, so recover that 
#  as state. Then look up the capital within it.

names = super_dict.keys()
for name in sorted(names):
    state = super_dict[name]
    capital = state['capital']
    print('   ',name,'->',capital)
    
