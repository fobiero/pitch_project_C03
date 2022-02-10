import email
from flask import render_template, url_for, flash, redirect
from app.forms import RegForm, LogForm
from app import app, db, bcrypt
from app.models import User, Post
from flask_login import login_user

posts = [
    {
        'author': 'king fela', 
        'title': 'Business', 
        'content': 'Content for post One',
        'date_posted': 'April 20 , 2018'
    },
    {
        'author': 'Oject Object', 
        'title': 'Politics', 
        'content': 'Content for post Two',
        'date_posted': 'March 20 , 2020'
    },
    {
        'author': 'Paul Sign', 
        'title': 'LifeStyle', 
        'content': 'Content for post Three',
        'date_posted': 'July 20 , 2001'
    }
]

@app.route('/')
def home():
    title = 'HomePage'
    return render_template('home.html', title = title, posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html', title ='Register', form = form)

@app.route('/login' , methods=['GET', 'POST'])
def login():

    form = LogForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    
    return render_template('login.html', title ='Login', form = form)
