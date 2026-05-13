# Import Flask class from the flask package.
# Flask is the web framework we use to create the web application.
from flask import Flask

# Create the Flask application object.
# __name__ tells Flask where this application is located.
app = Flask(__name__)

# Define the home page route.
# When someone opens http://localhost:5000/, this function will run.
@app.route("/")
def home():
    # Return simple text to the browser or curl.
    return "Hello from Flask CI/CD app!"

# Define the health check route.
# CI/CD, Docker, and Kubernetes can use this endpoint to check if the app is alive.
@app.route("/health")
def health():
    # Return "OK" with HTTP status code 200.
    # 200 means the application is healthy and working.
    return "OK", 200

# This block runs only when we start the file directly with: python app.py
# It does not run when Gunicorn imports the app in Docker.
if __name__ == "__main__":
    # Start the Flask development server.
    # host="0.0.0.0" means the app listens on all network interfaces.
    # port=5000 means the app listens on TCP port 5000.
    app.run(host="0.0.0.0", port=5000)