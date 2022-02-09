from flask import Flask, render_template, url_for, flash, redirect
from forms import RegForm, LogForm

app = Flask(__name__)

posts = [
    {
        'author': 'king fela', 
        'title': 'Post One', 
        'content': 'Content for post One',
        'date_posted': 'April 20 , 2018'
    },
    {
        'author': 'Oject Object', 
        'title': 'Post Two', 
        'content': 'Content for post Two',
        'date_posted': 'March 20 , 2020'
    }
]

app.config['SECRET_KEY'] = '4963fe5782355fc76e4821f231207f5f14216e10'

@app.route('/')
def home():
    title = 'HomePage'
    return render_template('home.html', title = title, posts=posts)

@app.route('/about')
def about():
    title = 'AboutPage'
    return render_template('about.html', title = title)

@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegForm()
    if form.validate_on_submit():
        flash(f'Account for {form.username.data} is created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title ='Register', form = form)

@app.route('/login' , methods=['GET', 'POST'])
def login():

    form = LogForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == 'admin':
            return redirect(url_for('home'))
    return render_template('login.html', title ='Login', form = form)

if __name__  == '__main__':
    app.run(debug=True)
