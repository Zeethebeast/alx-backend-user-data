#!/usr/bin/env python3
"""
Route module for the API.

This module initializes and configures the
Flask application, registers blueprints,
and sets up CORS support and error handlers
for custom HTTP responses.

Environment variables:
    API_HOST (str): Host address to listen on (default: 0.0.0.0).
    API_PORT (int): Port to listen on (default: 5000).
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS

# Initialize Flask application
app = Flask(__name__)

# Register the blueprint containing API routes
app.register_blueprint(app_views)

# Set up CORS (Cross-Origin Resource Sharing) to allow access from any origin
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error) -> str:
    """
    Handle 404 Not Found errors.

    Returns:
        JSON response with a 404 error message.
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Handle 401 Unauthorized errors.

    Returns:
        JSON response with a 401 error message.
    """
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")

    # Run the application
    app.run(host=host, port=port)
