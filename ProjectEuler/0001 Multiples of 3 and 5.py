# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# Answer: 233168

def SumMultiple(mult, limit):
    total = 0
    totsum = (limit-1) // mult
    num = 0
    while num <= totsum:
        total += num
        num += 1
    total *= mult
    return total

print(SumMultiple(3,1000)+SumMultiple(5,1000)-SumMultiple(15,1000))

def SumMultiple2(number1, number2, limit):
    i = 0
    total = 0
    while i < limit:
        if i % number1 == 0 or i % number2 == 0: total += i
        i += 1
    return total

print (SumMultiple2(3, 5, 1000))