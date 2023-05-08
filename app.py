from flask import Flask
from flask_cors import CORS
from .templates.routes import hangman
from main import Game

app = Flask(__name__)
CORS(app)

app.register_blueprint(hangman)