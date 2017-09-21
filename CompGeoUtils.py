import numpy as np
import matplotlib.pyplot as plt


def to_np_array(filename: str):
    with open(filename, 'rt') as f:
        tempPoints = []
        for lineNumber, line in enumerate(f):
            if lineNumber != 0:
                x, y = line.split()
                tempPoints.append((float(x), float(y)))
    return np.array(tempPoints)


def left_of(a, b, c, Print=False):
    return area_of_triangle(a, b, c, Print) > 0


def right_of(a, b, c, Print=False):
    return area_of_triangle(a, b, c, Print) < 0


def area_of_triangle(p1, p2, p3, Print=False):
    # takes np.array points
    if Print:
        print("" + str(p1) + "," + str(p2) + "," + str(p3) + ":" + str(np.cross((p2 - p1), (p3 - p1)) / 2.))
    return np.cross((p2 - p1), (p3 - p1)) / 2.


def draw_hull(hull):
    for p, p_next in zip(hull, hull[1:]):
        print_points(hull, 'ro', 1)
        plt.plot([p[0], p_next[0]], [p[1], p_next[1]], 'r--')

    if len(hull) > 2:
        pass
        plt.plot([hull[-1][0], hull[0][0]], [hull[-1][1], hull[0][1]], 'r--')


def convex_hull(points):
    # sort and separate min and max x-coord's, add to hull
    x, y = zip(*points)
    points = points[np.lexsort([y, x])]
    hull = [points[0], points[-1]]

    # separate other points -- left and right of line x extrema
    left_pts, right_pts = [], []
    for p in points[1:-1]:
        if left_of(hull[0], hull[1], p):
            left_pts.append(p)
        else:
            right_pts.append(p)

    # TODO: function within function, revise
    def find_hull(s, p0, p1):
        if len(s) < 1:
            return
        else:
            # find point farthest from p0 and p1
            far_pt, max_area = s[0], 0.
            for pt in s:
                if abs(area_of_triangle(p0, p1, pt)) > max_area:
                    far_pt, max_area = pt, abs(area_of_triangle(p0, p1, pt))

            # insert farthest point between p0 and p1
            # TODO: simplify
            for i in range(0, len(hull)):
                if np.array_equal(hull[i], p1) and not np.array_equal(hull[i-1], far_pt):
                    hull.insert(i, far_pt)

            # find hulls for points outside of triangle
            out_left, out_right = [], []
            for pt in s:
                if not np.array_equal(pt, far_pt):
                    if right_of(p0, far_pt, pt):
                        out_right.append(pt)
                    if left_of(p1, far_pt, pt):
                        out_left.append(pt)

            # recursive call -- divide and conquer remaining hulls
            find_hull(out_right, p0, far_pt)
            find_hull(out_left, far_pt, p1)
    # END def

    # split hull in half based on extrema, recursively call find_hull
    find_hull(right_pts, hull[0], hull[1])
    find_hull(left_pts, hull[-1], hull[0])
    print_points(points, 'bo')
    draw_hull(hull)


def print_points(points, color='ro', z=0):
    x, y = zip(*points)
    plt.plot(x, y, color, zorder=z)

