"""
Leap Year:

A year is called a leap year if it contains an additional day which makes the number of the days in that year to be 366.
This additional day is added in February which makes it 29 days long.

A leap year occurs once every 4 years.

How to determine if a year is a leap year?

You should follow the following steps to determine whether a year is a leap year or not.

If a year is evenly divisible by 4 means having no remainder then go to next step. If it is not divisible by 4.
It is not a leap year. For example: 1997 is not a leap year.
If a year is divisible by 4, but not by 100. For example: 2012, it is a leap year. If a year is divisible by both 4 and 100, go to next step.
If a year is divisible by 100, but not by 400. For example: 1900, then it is not a leap year. If a year is divisible by both,
then it is a leap year. So 2000 is a leap year.
"""
Year = int(input("Enter a year:"))
if(Year % 4) == 0:
    if(Year % 100) == 0:
        if(Year % 400) == 0:
            print("{0} is a Leap year".format(Year))
        else:
            print("{0} is not a Leap Year".format(Year))
    else:
        print("{0} is a Leap Year".format(Year))
else:
    print("{0} is not a Leap Year.".format(Year))