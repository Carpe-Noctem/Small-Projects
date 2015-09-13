"""
This was one of my first "major" scripts that I created, and
I finally decided to upload it. The "Time Till" script is intended to
be a basic date-countdown program. The user inputs the month, day, and
year of the date they desire, and the program will give an estimeate of the
time remaining unitl it occurs. I plan on "cleaning" it up soon; e.g.,
actually adding commments, because even I have no memory of this place.
"""


from datetime import datetime # Importing the datetime module

now = datetime.now()

print "Welcome to my Date Countdown program!" # Welcome statement

print "\n\tThe current date is {0}/{1}/{2}.".format(now.year, now.month,now.day)

def time_till():
    while True:
        try:
            future_year = raw_input("\nWhat year would you like to countdown "
            "to? (Numerical format) ")
            future_year = int(future_year)
            future_month = raw_input("\nWhat month would you like to countdown "
            "to? (Numerical format) ")
            future_month = int(future_month)
            future_day = raw_input("\nWhat day would you like to countdown to? "
            "(Numerical format) ")
            future_day = int(future_day)
        except ValueError:
            print "\nEnter your values in a numerical format"
            continue
        if len(str(future_year)) != 4 or not (1 <= future_month <= 12) or \
        not (1 <= future_day <= 31):
            print "\n\tInput a valid year, month, or day"
            continue
        else:
            break
    PD = "\n\tYou have already passed that date." # Passed Date; later used variable
    DT = "\n\tThat date is today." # Date Today; variable to be used later
    till_year = future_year - now.year
    till_month = future_month - now.month
    till_day = future_day - now.day
    XT = "\n\tThere are {0} year(s), {1} month(s), and {2} day(s) until your " \
    "date!" .format(till_year, till_month, till_day)
    if till_year < 0: # Any years behind the current one; automatically passed
        print PD
    elif till_year == 0: # Future date is in the current year
        if till_month == 0 and till_day == 0: # Same date
            print DT
        elif (till_month <= 0 and till_day <= 0) or \
        (till_month <= 0 and till_day >= 0): # Month has been passed and day is
            print PD                         # either ahead or behind
        elif till_month == 0 and till_day > 0: # Same month; day is ahead
            print XT
        elif (till_month > 0 and till_day > 0) or \
        (till_month > 0 and till_day == 0): # Month is ahead and the day is
            print XT                        # either ahead or the same
        elif till_month > 0 and till_day < 0: # Month is ahead; day is behind
            till_y = till_year
            till_m = till_month - 1
            till_d = till_day + 30
            print "\n\tThere are %s year(s), %s month(s), and %s day(s) until" \
            " your date!" % (till_y, till_m, till_d)
    elif till_year >= 1: # Year is ahead
        if till_month == 0 and till_day == 0: # Same month; same day
            print XT
        elif till_month > 0 and till_day > 0: # Month is ahead; day is ahead
            print XT
        elif till_month > 0 and till_day < 0: # Month is ahead; day is behind
            till_y = till_year
            till_m = till_month - 1
            till_d = till_day + 30
            print "There are %s year(s), %s month(s), and %s day(s) until" \
            " your date!" % (till_y, till_m, till_d)
        elif till_month > 0 and till_day == 0: # Month is ahead; day is same
            print XT
        elif (till_month <= 0 and till_day <= 0) or \
        (till_month <= 0 and till_day >= 0):#Month behind/same; day behind/ahead
            if till_month == 0 and till_day > 0: # Month is same; day is ahead
                print XT
            elif till_year <= 1: # Year is less than or equal to one
                till_m = (till_year * 12) + (till_month - 1)
                till_d = till_day + 30 # Assuming all months have 30 days
                till_y = till_year - 1
                print "There are %s year(s), %s month(s), and %s day(s) " \
                "until your date!" % (till_y, till_m, till_d)
            elif till_year > 1: # Year is greater than one
                till_m = (till_year * 12) + (till_month - 1) # Math to gain a
                till_year -= 1 * till_year # the correct values
                till_a = till_m // 12
                till_d = till_day + 30
                till_m = till_m - (till_a * 12)
                till_y = till_year + till_a
                print "There are %s year(s), %s month(s), and %s day(s) " \
                "until your date!" % (till_y, till_m, till_d)

time_till()
