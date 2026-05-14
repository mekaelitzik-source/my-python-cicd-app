# Import the Flask app object from app.py.
# First "app" = file name app.py.
# Second "app" = Flask object inside the file.
from app import app


# This test checks the home page route "/".
def test_home_page():
    # Create a test client.
    # The test client lets pytest call the Flask app without opening a real browser.
    client = app.test_client()

    # Send a fake HTTP GET request to the home page "/".
    response = client.get("/")

    # Check that the HTTP status code is 200.
    # 200 means the request was successful.
    assert response.status_code == 200

    # Check that the response text contains our expected message.
    assert b"Hello from Flask CI/CD app!" in response.data


# This test checks the health check route "/health".
def test_health_check():
    # Create a test client for the Flask app.
    client = app.test_client()

    # Send a fake HTTP GET request to "/health".
    response = client.get("/health")

    # Check that the HTTP status code is 200.
    assert response.status_code == 200

    # Check that the response text is OK.
    assert b"OK" in response.data
