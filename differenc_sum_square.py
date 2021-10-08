
#https://projecteuler.net/problem=6
import time
start=time.time()
sum = 0
sum_of_square = 0
for i in range(1,101):
    sum=sum+i
    sum_of_square = sum_of_square+i*i
square_of_sum = sum*sum
print(f"sum_of squares: {sum_of_square}")
print(f"square of sum: {square_of_sum}")
print(f"diff of square of sum and sum of square is : {square_of_sum - sum_of_square}")
elapsed=time.time()-start
print(f"elapsed {elapsed*1000} ms")