import numpy as np
import matplotlib.pyplot as plt

g = 9.8
c = 12.5
m = 68.1

t = np.arange(0, 14, 2)
temp = -(c/m)*t

V = ((g*m/c)*(1-np.exp(temp)))
print(V)

     