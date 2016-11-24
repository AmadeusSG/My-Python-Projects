# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# Answer: 6857

import time

# Own method, adapted from the internet

def LargestPrimeNo(number):
    i = 2
    while i <= number:
        if number % i == 0: number /= i
        else: i += 1
    return i

print("Method 1:")
start = time.perf_counter()
print(LargestPrimeNo(600851475143))
elapsed1 = time.perf_counter() - start
print("Elapsed in %s seconds\n" % elapsed1)
