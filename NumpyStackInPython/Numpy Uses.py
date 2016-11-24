#!/usr/bin/env python
import numpy as np
import time

###################################
# Lecture 3 - Lists vs Arrays     #
###################################
print("~~~ Lecture 3 - Lists vs Arrays ~~~\n")

L = [1,2,3]
print("L = [1,2,3]")
A = np.array([1,2,3])
print("A = np.array([1,2,3])\n")

# What both lists and arrays can do:
print("What both lists and arrays can do:")
# Reiteration of for loops
print("Reiteration of for loops\n")

def loop(list):
    for e in list:
        print(e)

start = time.perf_counter()
print ('Loop of list:')
loop(L)
elapsed1 = time.perf_counter() - start
print ("Elapsed in %s seconds\n" % elapsed1)

start = time.perf_counter()
print ('Loop of array"')
loop(A)
elapsed2 = time.perf_counter() - start
print ("Elapsed in %s seconds\n" % elapsed2)
factor = elapsed1/elapsed2
print ("Factor of %s\n" % factor)

# What only lists can do:
print("What only lists can do:")

# Appends
print("Appends: L.append(4)")
L.append(4)
print(L)

# Concaternate
print("Concaternate: L+=[5]")
L+=[5]
print(str(L) + "\n")

# Numpy Arrays cannot append nor it can add more elements like how lists can be done
print("Append on A will get an error like this:")
print("AttributeError: \'numpy.ndarray\' object has no attribute \'append\'\n")

# Differences
print("Differences:\n")
print("Addition of lists will get this:")
print("L + L = " + str(L+L) + "\n")
print("Addition of arrays will get this:")
print("A + A = " + str(A+A) + "\n")

print("Same with multiplication:")
print("2 * L = " + str(2*L))
print("2 * A = " + str(2*A) + "\n")

print("For multiplication on lists, you need to do a for loop:\n")

# For multiplication on lists
L1 = [1,2,3]
start = time.perf_counter()
L2 = []
for e in L1:
    L2.append(e + e)
print(L2)
elapsed1 = time.perf_counter() - start
print ("Elapsed in %s seconds for list loop\n" % elapsed1)

# For multiplication on arrays
start = time.perf_counter()
print(2*A)
elapsed2 = time.perf_counter() - start
print ("Elapsed in %s seconds for array multiplication\n" % elapsed2)
factor = elapsed1/elapsed2
print ("Factor of %s\n" % factor)

