"""
This minor challenge will showcase the sum of
of a number's values which are either divisible by
3 or 5.
"""


print 'Welcome to my "Multiples of 3 and 5" solution!'

sum = 0
i = int(raw_input("Input a range from 1 to your number to begin: "))


for num in range(i):
    if num % 3 == 0 or num % 5 == 0:
        sum += num

print "Your sum is {ts}.".format(ts = sum)
