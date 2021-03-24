from app import app

# these are Python decorators
# note the common pattern of a decorator creating an association between the
#  passed in URL and the function defined beneath it
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"