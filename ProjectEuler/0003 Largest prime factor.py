# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# Answer: 6857

def LargestPrimeNo(number):
    i = 2
    while i <= number:
        if number % i == 0: number /= i
        else: i += 1
    return i

print(LargestPrimeNo(600851475143))