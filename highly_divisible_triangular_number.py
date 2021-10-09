import time
start=time.time()
def find_divisors(n):
    
    n_div=0
    
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            # divisors.append(i)
            n_div = n_div+1
             
    return n_div*2

def triangulize(n):
    sum=0
    for i in range(n):
        sum=sum+i
    return sum


triangle =(triangulize(x) for x in range(10000,100000))
count=0
found=0

for item in triangle:
    count=find_divisors(item)
    if count>500:
        print(count,item)
        break

        
elapsed=time.time()-start
print(f" first Integer with {count} divisors,  triangle: {found} in {elapsed*1000} ms")