from flask import Flask
from config import Config

# __name__ is a Python predefined variable

# don't confuse the app variable here with the
# app package imported from routes below
app = Flask(__name__)
# tells Flask to read + apply the Config class to the app var/Flask instance
app.config.from_object(Config)

# note that this import must be beneath the app variable definition
# as the app package requires the app variable to be defined
from app import routes
