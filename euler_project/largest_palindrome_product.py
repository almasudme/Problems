#largest_palindrome_product.py
import time

def is_palindrome(n):
    strn=str(n)
    length=len(strn)
    for i in range(int(length/2)):
        if strn[i] != strn[length-1-i]:
            return False
    return True


if __name__ == "__main__":
    start = time.time()
    break_var = False
    max_pal=0
    for i  in range(999,100,-1):
        for j in range(999,100,-1):
            product=i*j
            if is_palindrome(product) and product>max_pal:
                max_pal = product

    elapsed=time.time() -start
    print(f"largest palindrome is {max_pal}, elapsed= {elapsed*1000} ms")


