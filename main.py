from CompGeoUtils import *


# Generate points
#arr = to_np_array('input.txt')
x, y = np.random.randint(0, 200, 30), np.random.randint(0, 200, 30)
arr = np.array([*zip(x, y)], dtype=float)

# Compute Convex Hull
convex_hull(arr)

# Plot results
plt.show()


