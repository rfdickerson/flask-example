
from flask import jsonify
from server import app

@app.route("/health")
def health():
    """health route"""
    state = {"state": "success"}
    return jsonify(state)
