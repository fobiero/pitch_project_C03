
from distutils.errors import CompileError
from flask import render_template, url_for, redirect, request
from app.forms import RegForm, LogForm, Comment
from app import app, db, bcrypt
from app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

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
    }
]

@app.route('/')
def home():
    title = 'HomePage'
    posts = Post.query.all()
    return render_template('home.html', title = title, posts = posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LogForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    
    return render_template('login.html', title ='Login', form = form)

@app.route('/logout')
def logout():

    logout_user()
    return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():

    title = 'User Account'
    return render_template('profile.html', title = title)

@app.route('/post/new', methods=['GET', 'POST'])
def post_new():
    form = Comment()
    if form.validate_on_submit():
        post = Post(title = form.post_title.data, content = form.post_content.data, author = current_user)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('post.html', form = form)