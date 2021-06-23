from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import os
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('d_uri')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv('s_key')
db = SQLAlchemy(app)

from application import routes