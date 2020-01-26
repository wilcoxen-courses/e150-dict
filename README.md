# Exercise: Dictionary Basics

### Summary

Practice with basic operations involving dictionaries in Python.

### Instructions

The first part of this assigment is to build a script called `basics.py` 
that does the following.

1. Create four dictionaries called `ca`, `tx`, `fl`, and `ny`. They 
will be used to store information about the four US states with the largest
populations in 2016. Each dictionary should have three keys: `po` for the
state's two-letter postal code, `name` for its name, and `pop` for its
population. Use the information below to set the corresponding values for 
each dictionary:
    ```
    name         po  pop
    California:  CA  38654206
    Florida:     FL  19934451
    New York:    NY  19697457
    Texas:       TX  26956435
    ```
    To be clear, the data should be coded directly into the script: it is 
    not necessary to store it in a file and then read the file. Reading
    the data from a file is what would usually be done in a production 
    context but we'll wait do do that until part 2.

1. Print the `ny` dictionary.

1. Now create a list called `state_list` that has one element for each of the states. That is, it should consist of the four dictionaries created above: 
`ca`, `tx`, `fl`,`ny`.

1. Print `state_list`. Notice that it's a list of four elements and each 
element is itself a dictionary.

1. Add a variable called `uspop` that is equal to 317899153, which was the 
total population of the states in 2016 (it excludes Washington, DC, 
Puerto Rico, and other US territories).

1. Print a message `Percent of the US population:` to create a heading
for what comes next.

1. Loop through `state_list` using `state` as the running variable (the 
variable name following `for` in a for-loop). Within the loop, create 
variables `name` and `pop` that are equal to that state's name and 
population. Then create a variable called `po` that is equal to `(` plus 
the state's PO code, plus `)`, and a variable called `pct` that is equal 
to 100 times the ratio of the state's population to `uspop`. Then use a 
print statement to print out `name`,`po` and `pct` (one line per state).
Each line should look something like this:
    ```
    California (CA) 12.15926674708693
    ```
    Don't worry if your percentage is off in some of the last digits; 
    those would usually be trimmed off in a finished script.
    
For the second part of the assignment, build a script called `nato.py`
that does the following:

1. Create a variable called `natofile` equal to "nato-alphabet.txt".

1. Create an empty dictionary called `to_nato`.

1. Opens `natofile`.

1. Loops through the lines of the file doing the following to each line: 
first, use the `strip()` call to remove leading and trailing blank space;
then use the `lower()` call to convert it all to lower case; then split
the result into a list of words called `words`. Finally, use element 0 
of `words` (the letter) as a dictionary key and set the value of `to_nato`
for that key to `words` element 1 (the NATO word).

1. Create a variable called `syr_str` that is equal to "syracuse" and 
create an empty list called `syr_list`.

1. Use a for-loop to go through the letters in `syr_str`, look each one
up in `to_nato`, and then append that word to the end of `syr_list`.

1. Then join `syr_list` with spaces and print out a message with `syr_str`,
"is:", and then the joined list of NATO words.

1. Create a variable `my_str` equal to your first name in lower case, and 
then repeat the last couple of steps to translate it into its phonetic 
alphabet equivalent and print it out. 

### Submitting

Once you're happy with everything and have committed all of the changes to
your local repository, please push the changes to GitHub. At that point, 
you're done: you have submitted your answer.

### Tips

+ This just scratches the surface of what can be done with dictionaries. 
They are the most powerful and flexible of Python's data structures.

+ If you know how to define and use functions, you may want to set one 
up to translate a given string to its NATO equivalent and then print 
out the result. You could then call the function on `syr_str` and then 
`my_str` without having any duplicate code.