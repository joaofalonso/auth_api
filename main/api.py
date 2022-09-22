from flask_restx import Api
from flask import Flask

app = Flask(__name__)
api = Api(app, title = 'Auth Api', description = 'Implementation of Authentication using Flask and JWT')