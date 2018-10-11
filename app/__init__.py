from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
# login = LoginManager(app)

from app import routes