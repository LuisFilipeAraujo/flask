from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Luis'}
    posts = [
        {
            'author': {'username': 'Michael'},
            'body': 'Husky'
        },
        {
            'author': {'username': 'Jocelin'},
            'body': 'Poodle'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


''' 
render_template() function invokes the Jinja2 template engine that 
comes bundled with the Flask framework. Jinja2 substitutes {{ ... }} 
blocks with the corresponding values, given by the arguments provided 
in the render_template() call.
'''