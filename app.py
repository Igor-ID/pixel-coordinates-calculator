import ast
import numpy as np
from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def solution():
    # bmi = 'Please enter valid number'
    if request.method == 'POST':
        dimensions = request.form.get('dimensions')
        corner_points = request.form.get('corner_points')

        # Check if the user filled in all the required fields
        if dimensions == '' or corner_points == '':
            return render_template("index.html", err='Please fill in all required fields')

        # Get the appropriate class type from the input
        dimensions_set = ast.literal_eval(dimensions)
        corner_points_list = ast.literal_eval(corner_points)

        if type(dimensions_set) != tuple or type(corner_points_list) != list or len(corner_points_list) < 4:
            return render_template("index.html", err='Please follow the instructions when filling the form')

        corner_points_array = np.array(corner_points_list)

        # Assume that coordinates are positive numbers [0., inf)
        if (corner_points_array < 0).sum() > 0:
            return render_template("index.html", err='Coordinates must be positive numbers')

        # dimension == (rows(Y-axis), columns(X-axis))
        x_length = dimensions_set[1]
        y_length = dimensions_set[0]

        # Transpose corner_points to get X and Y arrays
        c_p_ar = corner_points_array.transpose()

        # get only unique coordinates, since corner points define a rectangle with sides parallel to the x and y axes
        x_coordinates = set(c_p_ar[0])
        y_coordinates = set(c_p_ar[1])

        # Get a list of start and end points for columns and rows
        x_points = sorted(x_coordinates)
        y_points = sorted(y_coordinates)

        # Get arrays of points on the X and Y axes
        x = np.linspace(x_points[0], x_points[1], x_length)
        y = np.linspace(y_points[0], y_points[1], y_length)

        # Get two matrices of X and Y coordinates and transpose to the required shape.
        res_temp = np.array(np.meshgrid(x, y)).transpose([1, 2, 0])

        # flip the result to get the answer from bottom left to upper right.
        result = np.flip(res_temp, 0)
        return render_template("index.html", result=result)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, passthrough_errors=True)

