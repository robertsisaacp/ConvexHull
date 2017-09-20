import matplotlib.pyplot as plt
import numpy as np

from CompGeoUtils import *


arr = to_np_array('input.txt')
x = np.random.randint(0, 20, 20)
y = np.random.randint(0, 20, 20)
xy = zip(x, y)
#arr = np.array([x, y])
#convex_hull(arr)
#plt.show()


print(arr)
print([x, y])
print(xy)
