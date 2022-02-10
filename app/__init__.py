import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

ENV = 'dev'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://moringa:root@localhost/moringa'
    app.config['SECRET_KEY'] = '4963fe5782355fc76e4821f231207f5f14216e10'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usersData.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from app import routes