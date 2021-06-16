import numpy as np

a = np.ones(10)
c = np.zeros(5)
d = np.append(a,c)
print(type(a))
print(a)
print(d)

print(d.tolist())