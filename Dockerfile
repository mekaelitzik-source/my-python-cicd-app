# Use official Python 3.11 slim image as the base image.
# This is the starting operating system + Python environment for our container.
FROM python:3.11-slim

# Set /app as the working directory inside the container.
# All next commands will run from this folder.
WORKDIR /app

# Copy requirements.txt from your computer into the container.
# We copy this first so Docker can cache the pip install layer.
COPY requirements.txt .

# Install all Python packages listed in requirements.txt.
# --no-cache-dir keeps the image smaller.
RUN pip install --no-cache-dir -r requirements.txt

# Copy app.py from your computer into the container.
# This gives the container your Flask application code.
COPY app.py .

# Document that the container application uses port 5000.
# This does not publish the port by itself; it only describes it.
EXPOSE 5000

# Start the app with Gunicorn when the container runs.
# --bind 0.0.0.0:5000 means listen on all container interfaces on port 5000.
# app:app means file app.py and Flask object named app.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]