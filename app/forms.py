from xml.dom import ValidationErr
from  flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class RegForm (FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')
    
    def if_username_exists(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user :
            raise  ValidationError('User already Exist!')

    def if_email_exists(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user :
            raise  ValidationError('Email is taken!')

class LogForm (FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')