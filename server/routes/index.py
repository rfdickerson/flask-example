
from server import app

@app.route("/")
def hello():
    """hello route"""
    return "Hello  World from Python!"
    