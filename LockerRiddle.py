from math import *

Number = 100
Lockers = [False]*Number

for i in range(Number):
    for j in range(i+1):
        if ((i+1) % (j+1) == 0):
            if Lockers[i]: Lockers[i] = False
            else: Lockers[i] = True

print(Lockers.count(True))
print(int(sqrt(Number)))