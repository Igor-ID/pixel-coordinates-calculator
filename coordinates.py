import numpy as np


def solution(dimension, corner_points):

    # Assume the coordinates are positive numbers [0., inf)
    # Check if the coordinates are positive numbers, since this condition is not specified in the requirements
    if (np.array(corner_points)<0).sum() > 0:
        return 'Coordinates must be positive numbers'

    # dimension == (rows(Y-axis), columns(X-axis))
    X_length = dimension[1]
    Y_length = dimension[0]

    # Transpose corner_points to get X and Y arrays
    c_p_ar = np.array(corner_points).transpose()

    # The corner points define a rectangle with sides parallel to the x and y axes, get only unique coordinates
    X_coordinates = set(c_p_ar[0])
    Y_coordinates = set(c_p_ar[1])

    # Get a list of start and end points for columns and rows
    X_points = sorted(X_coordinates)
    Y_points = sorted(Y_coordinates)

    # Get arrays of points on the X and Y axes
    X = np.linspace(X_points[0], X_points[1], X_length)
    Y = np.linspace(Y_points[0], Y_points[1], Y_length)

    # Get two matrices of X and Y coordinates and transpose into the required shape
    res_temp = np.array(np.meshgrid(X, Y)).transpose([1,2,0])

    # Flip the result to get the answer from bottom left to top right
    res = np.flip(res_temp, 0)

    return res


# corner_points = [
#     (1.5, 1.5),  # (x, y)
#     (4.0, 1.5),  # (x, y)
#     (1.5, 8.0),  # (x, y)
#     (4.0, 8.0)]
#
# dimension = (10, 12)  # (rows(Y-axis), columns(X-axis))

corner_points = [
    (0, 0),  # (x, y)
    (6.0, 0),  # (x, y)
    (0, 6.0),  # (x, y)
    (6.0, 6.0)]

dimension = (5, 5)  # (rows(Y-axis), columns(X-axis))

print(solution(dimension, corner_points))

