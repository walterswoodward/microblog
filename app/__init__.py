from flask import Flask

# __name__ is a Python predefined variable

# don't confuse the app variable here with the
# app package imported from routes below
app = Flask(__name__)

# note that this import must be beneath the app variable definition
# as the app package requires the app variable to be defined
from app import routes
