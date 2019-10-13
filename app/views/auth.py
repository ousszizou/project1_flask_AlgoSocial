from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from app.forms.users import LoginForm , RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models.users import User
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    title = 'login'
    form = LoginForm()
    if request.method == 'GET':
        return render_template('auth/login.html', title=title, form=form)

    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in DB
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    # it the abobe check passes, then we know the user has the right credentials
    login_user(user)
    session['username'] = current_user.username
    return redirect(url_for('home.home_page'))




@auth.route('/register', methods=['GET', 'POST'])
def register():
    title = 'register'
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('auth/register.html', title=title, form=form)

    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    # if this returns a user, then the email already exists in DB.
    user = User.query.filter_by(email=email).first()

    # if a user is found. we want to redirect back to register page so user can try again.
    if user:
        flash('Email Address already exists.')
        return redirect(url_for('auth.register'))

    # create a new user with the form data, hash the password so plaintext version isn't saved.
    if form.validate_on_submit():
        new_user = User(email=email,username=username,password=generate_password_hash(password,method="sha256"))
        # add the new user to DB.
        db.session.add(new_user)
        db.session.commit()

        flash('Thnaks for registration')
        return redirect(url_for('auth.login'))
    else:
        return render_template("auth/register.html", title=title, form=form)

@auth.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    logout_user()
    return redirect(url_for('home.home_page'))
