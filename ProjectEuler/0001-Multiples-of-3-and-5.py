# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# Answer: 233168

import time

# Initial way:
def SumMultiple(mult, limit):
    total = 0
    totsum = (limit-1) // mult
    num = 0
    while num <= totsum:
        total += num
        num += 1
    total *= mult
    return total

print("Method 1:")
start = time.perf_counter()
print(SumMultiple(3,1000)+SumMultiple(5,1000)-SumMultiple(15,1000))
elapsed1 = time.perf_counter() - start
print("Elapsed in %s seconds\n" % elapsed1)

# Another way found from the internet:
def SumMultiple2(number1, number2, limit):
    i = 0
    total = 0
    for i in range(limit):
        if i % number1 == 0 or i % number2 == 0: total += i
    return total

print("Method 2:")
start = time.perf_counter()
print (SumMultiple2(3, 5, 1000))
elapsed2 = time.perf_counter() - start
print("Elapsed in %s seconds\n" % elapsed2)

# Speed factor
factor = elapsed1/elapsed2
print("Method 2 is %s faster than Method 1" % factor)