from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
# Register form
class RegisterForm(FlaskForm):
    email = StringField(label="email", validators=[DataRequired(), Email()])
    username = StringField(label="username", validators=[DataRequired()])
    password = PasswordField(label="password", validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField(label="confirm", validators=[DataRequired(),EqualTo(fieldname='password')])
    submit = SubmitField(label="Register")

# login form
class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')
