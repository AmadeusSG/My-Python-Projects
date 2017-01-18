import random as rd

a, b = rd.randint(1,500), rd.randint(1,500)

### HCF ###
# Using loops
def HCFloop(x,y):
    if x > y: smaller = y
    else:     smaller = x

    for i in range(1, smaller+1):
        if((x % i)==0 and (y % i)==0 ): hcf = i
    return hcf

# Using the Euclidean algorithm
def HCF(x, y):
    while(y): x, y = y, x % y
    return x

### LCM ###
# Using loops
def LCMloop(x, y):
   if x > y: greater = x
   else:     greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

# Using Euclidean algorithm
def LCM(x, y):
    return (x*y)//HCF(x,y)

while(True):
    a, b = rd.randint(1, 500), rd.randint(1, 500)

    print("What is the HCF of %i and %i?" % (a,b))
    c = int(input())
    if (c == HCF(a,b)): print("Correct! \n")
    else: print("Wrong! The answer is %i. \n" % HCF(a,b))

    print("What is the LCM of %i and %i?" % (a,b))
    c = int(input())
    if (c == LCM(a,b)): print("Correct! \n")
    else: print("Wrong! The answer is %i \n" % LCM(a,b))
