'''
For those unaware, a human's body constitution is measured by dividing
their weight by their height squared (slightly differs between metric and 
imperial systems). The returned value is known as a BMI (Body Mass Index). 
BMR (Basal Metabolic Rate) is defined as the aggregate of calories one would 
"burn" if one decided to stay in bed all day; BMR, alongside activity level, is 
crucial to calculating a person's caloric needs. This program is meant to act as
a simple BMI and calorie calculator. The user inputs a few variables (weight, 
height, age, and gender) and is returned a BMI value and a general grade
classification based on it; and an estimate of their daily caloric needs.
'''

from __future__ import division # Importing the proper modules

print "Welcome to my BMI and calorie calculator!" # Welcome statement

def bmr(weight, height, age, gender, system_choice):
    if system_choice == "I" and gender == "male":# Imperial male
        return 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
    elif system_choice == "I" and gender == "female":# Imperial female
        return 665 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    elif system_choice == "M" and gender == "male":# Metric male
        return 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    else:# Metric female
        return 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    
def bmi(weight, height, system_choice): # BMI function
    if system_choice == "I":
        return (((weight * 703) / (height ** 2))) # Imperial Formula
    else:
        return ((weight / (height ** 2)) * 10000) # Metric Formula

# We will utilize the Harris Benedict Formula for our calorie calculation
def HBF(BMR, num_act_level): 
    if num_act_level == "1":
        return BMR * 1.2
    elif num_act_level == "2":
        return BMR * 1.375
    elif num_act_level == "3":
        return BMR * 1.55
    elif num_act_level == "4":
        return BMR * 1.725
    else:
        return BMR * 1.9

def calcHealth():
    inp = "\n\tYour inputted " # Variable to be used later in the program
    while True:
        while True: # Finds weight, height and age
            try:
                weight = float(raw_input("\nPlease input your weight in "
                "pounds for imperial/kilos for metric: "))
                
                height = float(raw_input("\nPlease input your height in "
                "inches for imperial/centimeters for metric: "))
                
                age = float(raw_input("\nPlease input your age in "
                "years: "))

                weight = round(weight, 1) # Rounds each value to 1 decimal place
                height = round(height, 1)
                age = round(age,1)

            except ValueError: # Only allowing numbers; ValueError caused by
                print "\n\tNumerical characters only"              # float()
                continue
            else:
                break
            
        while True: # Finds gender
            gender = raw_input("\nPlease input your gender by number: "
            "\n\t1. Male \n\t2. Female")
            if gender in ["1", "2"]:
                if gender == "1":
                    gender = "male"
                    break
                else:
                    gender = "female"
                    break
            else:
                print "\nInput Error (acceptable values: ['1', '2'])"
                continue # The only allowed options
        
        while True: # Finds activity level
            act_level = raw_input("\nPlease input an approximation of your "
            "activity level by number: "
            "\n\t1. Sedentry (little or no exercise)"
            "\n\t2. Lightly active (light exercise/sports 1-3 days/week)"
            "\n\t3. Moderatetely active (moderate excercise/sports 3-5 days/"\
            "week)"
            "\n\t4. Very active (hard exercise/sports 6-7 days a week)"
            "\n\t5. Extra active (Very hard exercise/sports and physical job "\
            "or 2x training)")
            if act_level in ["1", "2", "3", "4", "5"]:
                break
            else:
                print "\nInput Error (acceptable values: ['1', '2', '3', '4', "\
                "'5'])"
                continue # The only allowed options

        num_act_level = act_level # Keeping only the number of act_level
        if act_level == "1":
            act_level = "\n\tsedentry (little or no exercise)"
        elif act_level == "2":
            act_level = "\n\tlightly active (light exercise/sports 1-3 days/"
            "week)"
        elif act_level == "3":
            act_level = "\n\tmoderatetely active (moderate excercise/sports " \
            "3-5 days/week)"
        elif act_level == "4":
            act_level = "\n\tvery active (hard exercise/sports 6-7 days a week)"
        else:
            act_level = "\n\textra active (Very hard exercise/sports and a" \
            "physical job or 2x training)"
            
        str_weight = str(weight)
        str_height = str(height)
        str_age = str(age)

        print inp + "weight is " + str_weight
        print inp + "height is " + str_height
        print inp + "age is " + str_age
        print inp + "gender is " + gender
        print inp + "activity level is " + act_level

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

    BMR = bmr(weight, height, age, gender, system_choice) # Calculates BMR
    BMI = bmi(weight, height, system_choice) # Calculates BMI
    CalorieCount = HBF(BMR, num_act_level) # Calculates daily calorie needs

    BMR = round(BMR, 1)
    BMI = round(BMI, 1)
    CalorieCount = round(CalorieCount, 1)

    print inp + "weight is " + str_weight
    print inp + "height is " + str_height
    print inp + "age is " + str_age
    print inp + "gender is " + gender
    print inp + "activity level is " + act_level
    print "\n\tYour calculated BMR is " + str(BMR) + " calories"
    print "\n\tYour calculated daily calorie needs is " + str(CalorieCount) + \
    " calories per day. \n\t(reduce by 200 to lose weight, maintain to keep an"\
    " even weight, and increase by 200 to gain weight)."
    print "\n\tYour calculated BMI is " + str(BMI)

    if BMI < 18.5:
        print "\n\tYou are underweight (BMI < 18.5)."
    elif 18.5 < BMI < 24.9:
        print "\n\tYou are at a normal weight (18.5 < BMI < 24.9)."
    elif 25.0 < BMI < 29.9:
        print "\n\tYou are overweight (25.0 < BMI < 29.9)."
    elif 30.0 < BMI < 34.9:
        print "\n\tYou are at class I obesity (30.0 < BMI < 34.9)."
    elif 35.0 < BMI < 39.9:
        print "\n\tYou are at class II obesity (35.0 < BMI < 39.9)."
    else:
        print "\n\tYou are at class III obesity (BMI >= 40.0)."

calcHealth()
