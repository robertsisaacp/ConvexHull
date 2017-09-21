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


def right_of(a, b, c):
    return not left_of(a, b, c)


def area_of_triangle(p1, p2, p3):
    # takes np.array points
    return np.cross((p2 - p1), (p3 - p1)) / 2.


def draw_triangle(p1, p2, p3, **kwargs):
    tmp = np.vstack((p1, p2, p3))
    x, y = [x[0] for x in zip(tmp.transpose())]
    plt.fill(x, y, **kwargs)
    plt.show()


def draw_hull(hull):
    # sort by x value
    #hull.sort()
    print(type(hull))
    r = np.array(hull)

    for p, p_next in zip(hull, hull[1:]):
        print_points(hull, 'ro', 1)
        plt.plot([p[0], p_next[0]], [p[1], p_next[1]], 'r--')

    if len(hull) > 2:
        pass
        plt.plot([hull[-1][0], hull[0][0]], [hull[-1][1], hull[0][1]], 'r--')


def convex_hull(points):
    # separate min and max x-coord's and add to hull
    hull = [points[0], points[-1]]


    # separate other points into halves -- left and right of line made by x extrema
    left_pts, right_pts = [], []
    for p in points[1:-1]:
        if left_of(hull[0], hull[1], p):
            left_pts.append(p)
        else:
            right_pts.append(p)

    def find_hull(s, p0, p1):
        if len(s) < 1:
            return
        else:
            # TODO: memoize, change to list comprehension
            # find point farthest from p0 and p1
            far_pt, max_area = s[0], abs(area_of_triangle(p0, p1, s[0]))
            for pt in s[1:]:
                if (abs(area_of_triangle(p0, p1, pt)) > max_area):
                    far_pt = pt

            # insert farthest point into hull between p0 and p1
            hull.append(far_pt)

            # find remaining points (inside triangle, outside-left, outside-right)
            out_left, out_right = [], []
            for pt in s:
                # Don't include far_pt
                if abs(far_pt[0] - pt[0]) > 0 and abs(far_pt[1] - pt[1]) > 0:
                    if right_of(p0, far_pt, pt):
                        out_right.append(pt)
                    if left_of(p1, far_pt, pt):
                        out_left.append(pt)
            # recursive call -- divide and conquer
            find_hull(out_right, p0, far_pt)
            find_hull(out_left, p1, far_pt)
    # END def

    find_hull(right_pts, hull[0], hull[1])
    find_hull(left_pts, hull[1], hull[0])

    print_points(right_pts, 'bo')
    print_points(left_pts, 'go')
    draw_hull(hull)


def print_points(points, color='ro', z=0):
    x, y = zip(*points)
    plt.plot(x, y, color, zorder=z)

