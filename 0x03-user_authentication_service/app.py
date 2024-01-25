#!/usr/bin/env python3
"""
A simple flask app with user authentication features
"""
from flask import Flask, jsonify, request, abort, redirect

from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def inde() -> str:
    """GET/ returns the homepage payload"""
    return jsonify({"message": "Bienvenue"})


# @app.route("/users", methods=["POST"], strict_slashes=False)
# def users() -> str:
#    """returns the ac

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
