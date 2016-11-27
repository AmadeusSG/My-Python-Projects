# The sum of the squares of the first ten natural numbers is,
#
#               1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
#           (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.
#
# Answer: 25164150

import time

# Method 1: Own method

def DiffSumSqSum(limit):
    sumsquare = 0
    squaresum = 0

    i = 1
    while i <= limit:
        sumsquare += i**2
        squaresum += i
        i += 1
    squaresum **= 2
    return squaresum-sumsquare

print("Method 1:")
start = time.perf_counter()
print(DiffSumSqSum(100))
elapsed1 = time.perf_counter() - start
print("Elapsed in %s seconds\n" % elapsed1)
