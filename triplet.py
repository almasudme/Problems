# brute force
import time
start = time.time()
def triplet_brute():
    limit=1000
    
    for i in range(1,limit):
        for j in range(i+1,limit):
            for k in range(j,limit):
                if (i*i+j*j==k*k) and (i+j+k==1000):
                    print (f"{i,j,k}")
                    print(f"product: {i*j*k}")
                    break

def triplet_nsquare():
    from math import sqrt
    squares = [x*x for x in range(0,1000) ]
    max_squares = squares[-1]
    for i in range(0,1000):
        for j in range(0,1000):
            k = sqrt(squares[i]+squares[j])
            _val = k - int(k)
            k=int(k)
            if i!=0 and j !=0 and _val == 0 and i+j+k == 1000:
                print(i ,j, int(k) )
                print(f"product: {i*j*k}")
# triplet_brute()46281 ms
#triplet_nsquare()763 ms
elapsed=time.time() - start
print(f"elapsed: {elapsed*1000} ms")

            
