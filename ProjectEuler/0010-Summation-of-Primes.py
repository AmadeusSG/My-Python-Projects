# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
# Answer:

def sumprimes_sieve(limit):
    p_n = limit
    sieve = [True] * p_n                 # everything is prime to start
    count = 0
    for i in range(2, p_n):
        if sieve[i]:  # still prime?
            count += i  # sum it!
            for j in range(2 * i, p_n, i):  # cross off all multiples of i
                sieve[j] = False
    return count

print (sumprimes_sieve(2000000))