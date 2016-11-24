# A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Answer: 906609

import time

# Own method
def LPF(lowerlimit, upperlimit): # LPF: Largest Palindrome Finder
    a = lowerlimit
    b = lowerlimit
    answer = 0

    while a < upperlimit:
        while b < upperlimit:
            product = a * b
            if str(product) == str(product)[::-1] and product > answer:
                answer = product
                a2 = a
                b2 = b
            b += 1
        a += 1
        b = 1

    return [a2, b2, answer]

print("Method 1:")
start = time.perf_counter()
a = LPF(100,1000)
print("%s * %s = %s" % (a[0],a[1],a[2]))
elapsed1 = time.perf_counter() - start
print("Elapsed in %s seconds\n" % elapsed1)

# Found from internet

def find_max_palindrome(minlimit=99,maxlimit=999):
    max_palindrome = 0
    a = maxlimit
    while a > minlimit:
        b = maxlimit
        while b >= a:
            prod = a*b
            if prod > max_palindrome and str(prod)==(str(prod)[::-1]):
                max_palindrome = prod
                a2 = a
                b2 = b
            b -= 1
        a -= 1
    return [a2, b2, max_palindrome]

print("Method 2:")
start = time.perf_counter()
a = find_max_palindrome()
print("%s * %s = %s" % (a[0],a[1],a[2]))
elapsed2 = time.perf_counter() - start
print("Elapsed in %s seconds\n" % elapsed2)

# Speed factor
factor = elapsed1/elapsed2
print("Method 2 is %s faster than Method 1" % factor)