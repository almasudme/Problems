"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

n=0 
dow=2
months = [31,28,31,30,31,30,31,31,30,31,30,31]
for year in range(1901,2000+1):
    months[1]=28+(year%4==0 and year %100!=0 or year%400==0)
    for date in months:
        dow=dow+date%7
        if (dow%7 ==0): n = n+1

print(n)
