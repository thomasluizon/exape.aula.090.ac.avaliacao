from flask import render_template
from . import main

from ..models import User, Role
from flask_login import current_user

@main.route('/')
def index():
    if (current_user.is_authenticated):
        user_all = User.query.all();
        return render_template('index.html', user_all=user_all);
    return render_template('index.html');


'''
@main.route('/')
def index():
    user_all = User.query.all();
    return render_template('index.html')
'''

