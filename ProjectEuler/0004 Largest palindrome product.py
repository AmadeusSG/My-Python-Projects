# A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Answer: 906609

a = 1
b = 1
answer = 0

while a < 1000:
    while b < 1000:
        product = a * b
        if str(product) == str(product)[::-1] and product > answer:
            answer = product
            a2 = a
            b2 = b
        b += 1
    a += 1
    b = 1

print (str(a2) + " * " + str(b2) + " = " + str(answer))