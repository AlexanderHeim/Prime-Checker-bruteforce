
def isPrime(x):
    if not isinstance(x, int): #Only natural numbers can be prime numbers.
        return False
    if x == 1: # If x is 1 it is not prime.
        return False
    if x == 2 or x == 3:    #If x is 2 or 3 it is prime.
        return True
    if x % 2 == 0 or x % 3 == 0: #We check if x is a multiple of 2 or 3 here,
        return False             #because 2 and 3 are the only prime numbers not in the form of 6k+1 or 6k-1.
    i = 5
    while(i * i <= x):                   #We only check up to the squareroot of x because:
        if x % i == 0 or x % (i+2) == 0: #if x = p1*p2 and p2>p1 then p1 must be smaller than the squareroot of x,
            return False                 #and if p1=p2, p1 = sqrt(x)
        i += 6                           # We increase i by 6 because every prime larger than 3
    return True                          # can be written as 6k+1 or 6k-1
