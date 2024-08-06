# Facebook Tracking App

A simple Flask application to track profile views by logging requests to an image served by the app. The image is posted on a Facebook profile to log profile views when the image is requested. This effectively tracks the user-agent of the request, but the IP address remains the same because the request is handled by Facebook itself.

## Features

- Logs IP address, User-Agent, Referrer, HTTP method, and query parameters.
- Serves as a tracking image and logs each request.

## Requirements

- Python 3.x
- Flask
- Gunicorn

## How to use

1. Deploy this Flask app on any server
2. Copy the public URL route and post it on Facebook
3. Check the log files for details
