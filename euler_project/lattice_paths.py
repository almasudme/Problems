"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


"""
#analytical approach
#20 down path and 20 right path 
# we have to select 20 down paths from 40 down+right paths
#40c20 is the answer 40!/20!*20!

def factorial(n):
    if n==0:
        return 1
    else: 
        return n*factorial(n-1)

print(f"total paths = {factorial(40)/(factorial(20))**2}")


