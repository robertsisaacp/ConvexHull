import numpy as np
import matplotlib.pyplot as plt


def to_np_array(filename: str):
    with open(filename, 'rt') as f:
        tempPoints = []
        for lineNumber, line in enumerate(f):
            if lineNumber != 0:
                x, y = line.split()
                tempPoints.append((float(x), float(y)))
    return np.array(sorted(tempPoints))


def left_of(a, b, c):
    return area_of_triangle(a, b, c) > 0


def area_of_triangle(p1, p2, p3):
    return np.cross((p2 - p1), (p3 - p1)) / 2.


def draw_triangle(p1, p2, p3, **kwargs):
    tmp = np.vstack((p1, p2, p3))
    x, y = [x[0] for x in zip(tmp.transpose())]
    plt.fill(x, y, **kwargs)
    plt.show()


def convex_hull(points):
    hull, s1, s2= [], [], []
    a, b = points[0], points[-1]

    hull.append(a)
    hull.append(b)
    for p in points[1:-1]:
        if left_of(a, b, p):
            s2.append(p)
        else:
            s1.append(p)

    print_points(hull, 'bo', 1)
    print_points(s1, 'ro')
    print_points(s2, 'go')


def print_points(points, color='ro', z=0):
    x, y = zip(*points)
    plt.plot(x, y, color, zorder=z)
    #plt.show()


#def plot_hull(points, random=False):
#    if random:
#        x = np.random.random(20)
#        y = np.random.random(20)
#    else:
#        x, y = zip(*points)
#        test = [[], []]
#    plt.plot(x, y, 'r', zorder=1, lw=3)
#    plt.scatter(x, y, s=120, zorder=2)
#    plt.title('Demo')
#    plt.show()


#def angle_from_points(point, center):
#    # calculate angle between points and x-axis
#    delta = point - center
#    angle = np.arctan(delta[1] / delta[0])
#    if delta[0] < 0:
#        angle += np.pi
#    return angle


#def divide_hull(_points):
#    lpoints, rpoints, center = [[], []], [[], []], _points.mean(1)
#
#    for point in zip(_points[0], _points[1]):
#        if point[0] < center[0]:
#            lpoints[0].append(point[0])
#            lpoints[1].append(point[1])
#        else:
#            rpoints[0].append(point[0])
#            rpoints[1].append(point[1])
#    return [lpoints, rpoints]
