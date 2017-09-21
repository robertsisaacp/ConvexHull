from CompGeoUtils import *


# Generate or extract points
# arr = to_np_array('input.txt')
arr = np.array([*zip(np.random.randint(0, 200, 30),
                     np.random.randint(0, 200, 30))])

# Compute Convex Hull
convex_hull(arr)

# Plot results
plt.show()


