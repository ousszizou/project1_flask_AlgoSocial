from flask import Blueprint, render_template, request
from app.forms.users import LoginForm , RegisterForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    title = 'login'
    form = LoginForm()
    if request.method == 'GET':
        return render_template('auth/login.html', title=title, form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    title = 'register'
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('auth/register.html', title=title, form=form)
