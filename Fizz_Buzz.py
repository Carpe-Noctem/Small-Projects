"""
My take on the customary challenge most applicants face when 
applying for a programming job: "The FizzBuzz Challenge."
For those unaware of the rules, you must print out the numbers
from 1-100 with a catch: if the number is evenly divisible by 3,
print "Fizz"; if by 5 instead, print "Buzz"; and finally if by both,
print "FizzBuzz." This challenge is a nice project for beginners 
and veterans alike, and can be done in a wide array of languages.
"""

for number in range(1, 101): # Prints out numbers in range 1-101 exclusive
    if number % 3 == 0 and number % 5 == 0: # Check whether this statement is True before it reaches the others
        print "FizzBuzz"
    elif number % 3 == 0: # Using the modulo operator to check whether the number is evenly divisible by 3
        print "Fizz"
    elif number % 5 == 0: # Doing the same as above, but now using 5 instead
        print "Buzz"
    else: # If all else fails, print the number itself
        print number
