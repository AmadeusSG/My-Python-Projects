import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

def get_r2(X, Y):
    w = np.linalg.solve( X.T.dot(X), X.T.dot(Y) )
    Yhat = X.dot(w)

    d1 = Y - Yhat
    d2 = Y - Y.mean()
    r2 = 1 - d1.dot(d1) / d2.dot(d2)
    return r2

def TimeElapsed(ID, function):
    start = time.perf_counter()
    print("Method %s:" % ID)
    calc = function
    elapsed = time.perf_counter() - start
    print("Answer is %s, elapsed in %s seconds\n" % (calc, elapsed))
    return elapsed

