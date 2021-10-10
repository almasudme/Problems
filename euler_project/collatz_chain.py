import time

def collatz(n):
    # print(n,end=" ")
    step=0
    init=n
    while (n!=1):
        step=step+1
        if n%2 ==0:
            n=int(n/2)
        else:
            n=3*n+1
        # print(n,end=" ")
    # print("\n")
    return init,step

max_size=0
number=0
for i in range(1,1000000):
    init,step=collatz(i)
    if step>max_size:
        max_size=step
        number=init
        print(number,max_size,end="\n")