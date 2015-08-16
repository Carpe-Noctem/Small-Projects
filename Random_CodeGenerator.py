"""
The purpose of the Random Selectable-Length
Code Generator is to provide users an undemanding way to
make a random code completely on their own. Such codes
can be used for games or other reasons as desired by the user.
"""

import random # Importing the proper module (random)

print "Welcome to my Random Selectable-Length Code Generator!" # Welcome statement

def rc_generator(code):
    while True:
        s = raw_input("\nHow long would you like your code to be? "
        "(That is, how many characters?)")
        if not s.isdigit(): # Only accepting numerical values (e.g., 1, 20, etc.)
            print "\nDid you write a number? (Numerical characters only)"
            continue
        else:
            break
    s = int(s)
    v = 0
    while v < s:
        v += 1
        code = list(code) # Converts variable code into a list
        print random.choice(code), # Prints out the list in a random order

print rc_generator(raw_input("\nEnter a sequence to be turned into a random "
"code:")) # User's code
