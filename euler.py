"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def if_same_digit(number1,number2):
    max_number=max(number1,number2)
    min_number=min(number1,number2)
    dict_num1=dict()
    dict_num2=dict()
    for i in str(min_number):
        dict_num1[i]=1
    for j in str(max_number):
        dict_num2[j]=1

    for i in dict_num2.keys():
        try:
            dict_num1[i]==1
        except KeyError:
            return False

    return True


print(if_same_digit(123,321))

bFound=None
i = 100
while (bFound==None):
    
    if if_same_digit(i,2*i) and if_same_digit(i,3*i) and if_same_digit(i,4*i) and if_same_digit(i,5*i) and if_same_digit(i,6*i):
        bFound=i
        print(i)
    else:
        i=i+1