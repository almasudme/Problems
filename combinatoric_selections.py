import math
import time

start = time.time()
def factorial(n):
    if n == 0 or n==1:
        return 1
    if n>1:
        return n*factorial(n-1)
def combination(n,r):
    return factorial(n)/(factorial(n-r)*factorial(r))

print(combination(23,11)/1000000)

count_ncr=0
for i in range(1,101):
    if combination(i,int(i/2)) > 1000000:
        if i%2==0:
            count_ncr=count_ncr+1
            new_init=int(i/2)+1
        else:
            count_ncr=count_ncr+2
            new_init=int(i/2)+2
         
        for j in range(new_init,i):
            if combination(i,j) <=1000000:
                break
            else:
                print(combination(i,j))
                count_ncr = count_ncr+2
                
elapsed = time.time() - start
print(count_ncr)
print(f"elapsed = {elapsed*1000} ms")