# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
# Answer:232792560

import time

# Method 1: Getting the number through finding all the LCM of 1 to 20

print("Method 1:")
start = time.perf_counter()
print (2**3 * 3**2 * 5 * 7) # For smallest number from 1 to 10
print (2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19) # For smallest number from 1 to 20
elapsed1 = time.perf_counter() - start
print("Elapsed in %s seconds\n" % elapsed1)

# TODO: Create a globalfunction to generalise getting the LCM from 1 to k.
