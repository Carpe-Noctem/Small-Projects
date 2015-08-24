'''
For those unaware, a human's body
constitution is measured by dividing
their weight by their height squared.
The returned value is known as a
"Body Mass Index" or BMI. This program
is meant to act as a simple BMI calculator.
The user inputs a weight and height, and
is returned a BMI value and a general grade
classification based on it.
'''

from __future__ import division # Importing the proper modules


print "Welcome to my BMI calculator!" # Welcome statement

def calcBMI():
    inp = "\n\tYour inputted " # Variable to be used later in the program
    
    while True:
        while True:
            try:
                weight = float(raw_input("\nPlease input your weight in "
                "pounds for imperial or kilograms for metric: "))
                
                height = float(raw_input("\nPlease input your height in "
                "inches for imperial or centimeters for metric: "))
                
                weight = round(weight, 1) # Rounds each value to 1 decimal place
                
                height = round(height, 1)
                
            except ValueError: # Only allowing numbers; ValueError caused by
                print "\n\tNumerical characters only"              # float()
                continue
            else:
                break
              
        str_weight = str(weight)
        str_height =str(height)
        
        print inp + "weight is " + str_weight
        print inp + "height is " + str_height
        
        while True:
            system_choice = raw_input("\nDid you consistently use imperial "
            "units (I), metric units (M), or do you need to go back and change "
            "your options (B)? (I/M/B)")
            system_choice = system_choice.upper()
            if system_choice in ["I", "B", "M"]:
                break
            else:
                print "\nInput Error (acceptable values: ['I', 'M', 'B'])"
                continue # The only allowed options
              
        if system_choice in ["B"]: # Retrys the entire function again
            continue
        else:
            break
        
    if system_choice == "I":
        BMI = ((weight * 703) / (height ** 2)) # Imperial Formula
        
    elif system_choice == "M":
        BMI = (weight / (height ** 2)) # Metric Formula
        BMI *= 10000
        
    BMI = round(BMI, 1)
    
    print inp + "weight is " + str_weight
    print inp + "height is " + str_height
    print "\n\tYour calculated BMI is " + str(BMI)
    
    if BMI < 18.5:
        print "\n\tYou are underweight (BMI < 18.5)"
    elif 18.5 < BMI < 24.9:
        print "\n\tYou are at a normal weight (18.5 < BMI < 24.9)"
    elif 25.0 < BMI < 29.9:
        print "\n\tYou are overweight (25.0 < BMI < 29.9)"
    elif 30.0 < BMI < 34.9:
        print "\n\tYou are at class I obesity (30.0 < BMI < 34.9)"
    elif 35.0 < BMI < 39.9:
        print "\n\tYou are at class II obesity (35.0 < BMI < 39.9)"
    else:
        print "\n\tYou are at class III obesity (BMI >= 40.0)"
    
calcBMI()
