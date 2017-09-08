import numpy as np

def quickHull(listOfPoints):
    convexHull = set()
    # leftmostPoint, rightmostPoint = listOfPoints
    # Divide into left half A and right half B by x coords

    # Compute CH(A) and CH(B)

    # Combine CH’s of two halves(merge step)
    pass


with open('input.txt', 'rt') as f:
    tempPoints = []
    for lineNumber, line in enumerate(f):
        if lineNumber != 0:
            x, y = line.split()
            tempPoints.append((float(x), float(y)))

    # numpy array for (x, y) coordinates from temporary python list
    points = np.array(tempPoints)
    leftXIndex, rightXIndex = points[:, 0].argmin(), points[:, 0].argmax()
    
