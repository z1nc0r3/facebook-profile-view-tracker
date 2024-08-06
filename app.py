from flask import Flask, send_file, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename="profile_views.log", level=logging.INFO)


@app.route("/tracker")
def tracker():
    # Log the request details
    user_agent = request.headers.get("User-Agent")
    ip_address = request.remote_addr
    
    if not "facebookexternalhit" in user_agent:
        logging.info(f"Profile view from IP: {ip_address}, User-Agent: {user_agent}")

    # Serve the tracking image
    return send_file("i_see_you.jpeg", mimetype="image/jpeg")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
