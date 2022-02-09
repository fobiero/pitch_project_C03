from flask import Flask, render_template, request, url_for
from forms import RegForm, LogForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '4963fe5782355fc76e4821f231207f5f14216e10'

@app.route('/')
def index():
    title = 'HomePage'
    return render_template('index.html', title = title)

@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegForm()
    return render_template('register.html', title ='Register', form = form)

@app.route('/login')
def login():

    form = LogForm()
    return render_template('login.html', title ='Login', form = form)

if __name__  == '__main__':
    app.run(debug=True)
