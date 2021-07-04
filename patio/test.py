import numpy as np

sides = list()
a = 10 / np.tan(np.pi / 18)
for n in range(18, 73):
    b = 10 / np.tan(np.pi / n)
    if b - a > 10:
        sides.append(n)
        a = b

print(sides)
