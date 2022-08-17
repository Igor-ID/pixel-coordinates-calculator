# pixel-coordinates-calculator
### Fetch Rewards Coding Assessment - Machine Learning Engineer
Task description see [here](https://fetch-hiring.s3.amazonaws.com/machine-learning-engineer/image-coordinates.html)

## Assumptions
1. Assume that coordinates are positive numbers [0., inf)
2. A mistake was made in the description.
- > the (x, y) coordinates of the four corner points to display the image at are: (1, 1), (3, 1), (1, 3), and (3, 3) then the program should calculate and return the coordinates: (1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), **~~(3, 1), (3, 2),~~** (3, 3)

- The coordinates must be: (1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)

3. An error was made in the Output Specifications section.
- > For example, the x coordinate of the pixel at the top left corner of the image would be accessed with solution[0, 0, 0] and the y coordinate of the pixel at the bottom right of the image would be accessed with **~~solution[3, 3, 1]~~**.
- In python, 3x3 matrix indices range from 0 to 2, hence index 3 is out of range. Should be rewritten as ..**solution[2, 2, 1]**

## Run the program

### 1. Pull the existing image from Docker Hub

Pull the prebuilt image and run with the `docker run` command

```
docker pull igordedkov/pixel_coordinates_calculator
```

```
docker run -d -p 5000:5000 igordedkov/pixel_coordinates_calculator:latest
```

### 2. Build a Docker container locally

Clone the current repository

```
git clone https://github.com/Igor-ID/pixel-coordinates-calculator
```

Build a Docker image

```
docker build -t pixel_coordinates_calculator .
```

Create a container from the image and run the application

```
docker run -d -p 5000:5000 pixel_coordinates_calculator
```

### 3. Run the application on a local python environment

Clone the current repository

```
git clone https://github.com/Igor-ID/pixel-coordinates-calculator
```

Install the package for creating a virtual environment

```
pip install virtualenv
```

Create a new virtual environment

```
virtualenv venv
```

Activate virtual environment

```
source venv/bin/activate
```

Install the dependencies written in requirements.txt

```
pip install -r requirements.txt
```

Run the application

```
flask run
```

When one of the above steps is completed, in your favorite browser go to http://localhost:5000 to play with the program.


![image](https://user-images.githubusercontent.com/69838126/185070391-713f48d0-e20f-45ee-a8f0-1813600eda8f.png)
