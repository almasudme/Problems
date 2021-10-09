"""
Problem 5: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

import time
start = time.time()
def is_devisible(n):
    for i in range(1,20):
        if n%i !=0: return False
    return True

def brute_force(n):
    while (is_devisible(n)==False):
        print(n)
        n=n+n
    return n
# brute_force(20)  : Half hour  

def component(n):
    comp=[]
    i=2
    while (n!=1):
        if n%i ==0:
            n=n/i
            comp.append(i)

            
        else:
            i=i+1

    return comp   

def lcm(n1,n2):
    if n1>n2:
        maxn=n1
        minn=n2
    else:
        maxn=n2
        minn=n1
    lcmn=maxn
    i=0
    while True:
        if lcmn%maxn==0 and lcmn%minn==0:
            break
            
        else:
            i=i+1
            lcmn = minn*i
    return lcmn
            
      
m = 1
for i in range(1,21):
    if m%i!=0:
        m = lcm(m,i)



print(f"least multiple is {m}: elapsed = {time.time()-start}")


