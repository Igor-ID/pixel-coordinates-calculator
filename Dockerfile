# Use the Python3.8 container image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the contents into the working dir
ADD . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Defined the command to start the container
CMD ["python3", "app.py"]