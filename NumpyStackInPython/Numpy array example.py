import numpy as np

X = []

for line in open("data_2d.csv"):
    row = line.split(',')
    sample = []
    for i in row:
        n = float(i)
        sample.append(n)
    X.append(sample)
X = np.array(X)
print(X)