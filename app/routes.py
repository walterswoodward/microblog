from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# these are Python decorators
# note the common pattern of a decorator creating an association between the
#  passed in URL and the function defined beneath it
@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'author': {'username': 'Gandhi'},
            'body': 'Happiness is when what you think, what you say, and what you do are in harmony.'
        },
        {
            'author': {'username': 'Mother Teresa'},
            'body': 'If you judge people, you have no time to love them.'
        }
    ]

    # Note the conditional statements in index.html that ensure user, if undefined
    # defaults to 'Stranger'
    return render_template('index.html', title='Home', user={'username': 'Walter'}, posts=posts)

@app.route('/hello')
def hello():
    return "Hello, World!"

# note the default second param value is ['GET']
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)