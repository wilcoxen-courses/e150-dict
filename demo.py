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

#  Now build a longer list by reading a CSV data file. Open
#  the file

fh = open('states.csv')

#  Create a new, blank list to hold the data

list2 = []

#  Loop through the file building a new dictionary for each
#  state and then adding it to the list.

for line in fh:

    #  Removes leading and trailing space from the line. Not strictly
    #  needed here but important when reading from a file and not
    #  splitting on blank space.

    line = line.strip()

    #  Split up the line

    parts = line.split(',')

    #  Store the result in a new dictionary for the current state.
    #  Call strip() on each piece to get rid of excess space at the
    #  start and end

    new_state = {
        'name':    parts[0].strip(),
        'capital': parts[1].strip(),
        'po':      parts[2].strip()
        }

    #  Add the new dictionary to the list

    list2.append( new_state )

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

