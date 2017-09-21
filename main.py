from CompGeoUtils import *


# Create points
arr = to_np_array('input.txt')
# x = np.random.randint(0, 20, 20)
# y = np.random.randint(0, 20, 20)


# Generate Convex Hull
convex_hull(arr)


# Plot results
# plt.plot([0, 3], [0, 3], 'r--')
plt.show()


