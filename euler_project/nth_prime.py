from math import sqrt

def is_prime(n):
    if n==1 or n==0:
        return False
    if n%2==0 and n !=2:
        return False
    else:
        for i in range(3,int(sqrt(n))+1,2):
            if n%i==0:
                return False
    return True

current=0
nth=0
sum_of_prime=0
while (current < 2000000):
    current= current+1
    if is_prime(current):
        nth=nth+1
        print(nth,current)
        sum_of_prime=sum_of_prime+current
print(sum_of_prime)




