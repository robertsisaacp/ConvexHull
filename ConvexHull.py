import numpy as np
import matplotlib.pyplot as plt


def angle_from_points(point, center):
    # calculate angle between points and x-axis
    delta = point - center
    angle = np.arctan(delta[1] / delta[0])
    if delta[0] < 0:
        angle += np.pi
    return angle


def draw_triangle(p1, p2, p3, **kwargs):
    tmp = np.vstack((p1, p2, p3))
    x, y = [x[0] for x in zip(tmp.transpose())]
    plt.fill(x, y, **kwargs)
    # plt.show()


def area_of_triangle(p1, p2, p3):
    return np.linalg.norm(np.cross((p2 - p1), (p3 - p1))) / 2.


def divide_hull(points):
    lpoints = [[], []]
    rpoints = [[], []]

    for point in zip(points[0], points[1]):
        if point[0] < center[0]:
            lpoints[0].append(point[0])
            lpoints[1].append(point[1])
        else:
            rpoints[0].append(point[0])
            rpoints[1].append(point[1])

    return [lpoints, rpoints]


# generate two arrays of randomized floats between 0 and 1
points = np.random.random_sample((2, 40))
center = points.mean(1)

left, right = divide_hull(points)[0], divide_hull(points)[1]

plt.clf()
plt.plot(left[0], left[1], 'ro')
plt.plot(right[0], right[1], 'bo')
# plt.plot(center[0], center[1], 'bo')
plt.show()
