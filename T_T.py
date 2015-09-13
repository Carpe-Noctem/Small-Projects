"""
This was one of my first "major" scripts that I created, and
I finally decided to upload it. The "Time Till" script is intended to
be a basic date-countdown program. The user inputs the month, day, and
year of the date they desire, and the program will give an estimeate of the
time remaining unitl it occurs. I plan on "cleaning" it up soon; e.g.,
actually adding commments, because even I have no memory of this place.
"""


from datetime import datetime
now = datetime.now()

print "Welcome to my Date Countdown program!"
print "The current date is {0}/{1}/{2}." .format(now.year, now.month, now.day)
W = 0

def time_till(future_date):
    future_date = raw_input("What date would you like to countdown to? "
"(YYYY/MM/DD)")
    PD = "You have already passed that date."
    DT = "That date is today."
    if len(future_date) == 10:
        till_year = int(future_date[:4]) - now.year
        till_month = int(future_date[5:7]) - now.month
        till_day = int(future_date[8:]) - now.day
        XT = "There are %s year(s), %s month(s), and %s day(s) until your date!" % \
        (till_year, till_month, till_day)
        if till_year < 0:
            till_year = 0
            till_month = 0
            till_day = 0
            print PD
        elif till_year == 0:
            if till_month == 0 and till_day == 0:
                print DT
            elif till_month == 0 and till_day > 0:
                print XT
            elif (till_month <= 0 and till_day <= 0) or \
            (till_month <= 0 and till_day >= 0):
                till_month = 0
                till_day = 0
                print PD
            elif (till_month > 0 and till_day > 0) or \
            (till_month > 0 and till_day == 0):
                print XT
            elif till_month > 0 and till_day < 0:
                till_y = till_year
                till_m = till_month - 1
                till_d = till_day + 30
                print "There are %s year(s), %s month(s), and %s day(s) until" \
                " your date!" % (till_y, till_m, till_d)
        elif till_year >= 1:
            if till_month == 0 and till_day == 0:
                print XT
            elif till_month > 0 and till_day > 0:
                print XT
            elif till_month > 0 and till_day < 0:
                till_y = till_year
                till_m = till_month - 1
                till_d = till_day + 30
                print "There are %s year(s), %s month(s), and %s day(s) until" \
                " your date!" % (till_y, till_m, till_d)
            elif till_month > 0 and till_day == 0:
                print XT
            elif (till_month <= 0 and till_day <= 0) or \
            (till_month <= 0 and till_day >= 0):
                if till_month == 0 and till_day > 0:
                    print XT
                elif till_year <= 1:
                    till_m = (till_year * 12) + (till_month - 1)
                    till_d = till_day + 30
                    till_y = till_year - 1
                    print "There are %s year(s), %s month(s), and %s day(s) " \
                    "until your date!" % (till_y, till_m, till_d)
                elif till_year > 1:
                    till_m = (till_year * 12) + (till_month - 1)
                    till_year -= 1 * till_year
                    till_a = till_m // 12
                    till_d = till_day + 30
                    till_m = till_m - (till_a * 12)
                    till_y = till_year + till_a
                    print "There are %s year(s), %s month(s), and %s day(s) " \
                    "until your date!" % (till_y, till_m, till_d)
    else:
        print "Did you put your date in the right format? " \
        "(Include 0's if necessary)"
        return time_till(future_date)

print time_till(W)
