# Problem 17:
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

# counting first hundread
#1-9,21-99
#9 times in each hundred * 10 times in each thousand
total=900*len("hundred")+9*99*len("and")+10*(9*(len("one")+len("two")+len("three")+len("four")+len("five")+len("six")+len("seven")+len("eight")+len("nine")) \
         +10* (len("twenty")+len("thirty")+len("forty")+len("fifty")+len("sixty")+len("seventy")+len("eighty")+len("ninety")) \
           +(len("eleven")+len("twelve")+len("thirteen")+len("fourteen")+len("fifteen")++len("sixteen")+len("seventeen")+len("eighteen")+len("nineteen")+len("twenty"))*1) \
               +100*(len("one")+len("two")+len("three")+len("four")+len("five")+len("six")+len("seven")+len("eight")+len("nine"))

print(total)
# above solution was worong 21143. https://www.mathblog.dk/project-euler-17-letters-in-the-numbers-1-1000/  :21124