"""basic Flask app entry"""

import os

from flask import Flask

PORT = int(os.getenv('PORT', 5000))

app = Flask(__name__)

from server import routes

    