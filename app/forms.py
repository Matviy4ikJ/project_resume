from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField, BooleanField, FileField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, EqualTo, Length, Email


# class RegistrationForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
#     password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#
#     submit = SubmitField('Sign Up')
#

class ProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    profession = StringField('Profession', validators=[DataRequired()])
    level = StringField('Level', validators=[DataRequired()])
    education = StringField('education', validators=[DataRequired()])
    soft_skills = StringField('soft_skills', validators=[DataRequired()])
    hard_skills = StringField('hard_skills', validators=[DataRequired()])
    lang = StringField('lang', validators=[DataRequired()])
    description = StringField('description', validators=[])
    image = FileField('image', validators=[])
    submit = SubmitField('Update Profile')


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[
        DataRequired(),
        Email(message="Enter a valid email address.")
    ])
    password = PasswordField("Password", validators=[
        DataRequired(),
        Length(min=4, )
    ])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class SignUpForm(FlaskForm):
    email = StringField("email", validators=[
        validators.DataRequired(),
        validators.Email()
    ])
    password = PasswordField("password", validators=[
        validators.DataRequired(),
        validators.Length(min=4),
    ])
    confirm_password = PasswordField("confirm_password", validators=[
        validators.DataRequired(),
        validators.EqualTo("password", )
    ])
    submit = SubmitField("Sign Up")
