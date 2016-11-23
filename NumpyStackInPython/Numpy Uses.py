import numpy as np

###################################
# Lecture 3 - Lists vs Arrays     #
###################################

L = [1,2,3]

A = np.array([1,2,3])

# What both lists and arrays can do:
# Reiteration of for loops

def loop(list):
    for e in list:
        print(e)
print('loop of list')
loop(L)
print('\nloop of array')
loop(A)


