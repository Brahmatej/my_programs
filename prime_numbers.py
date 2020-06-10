#finding primes
import math
import numpy as np
import time
def prime(a):
    if a==1:
        return Fals
    if a%2==0 and a>2:
        return False
    for i in range(2,math.floor(math.sqrt(a))+1):
        if a%i==0:
            return False
    return True
t0=time.time()
def get_primes(start,stop):
    prime_numbers=[]
    for j in range(start,stop+1):
        if prime(j):
            prime_numbers.append(j)
    print("Prime numbers : \n  ",prime_numbers,"\n",len(prime_numbers))
    return prime_numbers
k=get_primes(1000000000000,1000000001001)
t1=time.time() 
print("Time = "+str(t1-t0))
r=[k[0]/k[i] for i in range(len(k)-2)]
print(r)