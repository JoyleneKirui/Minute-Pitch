from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager 
from flask_fontawesome import FontAwesome

app = Flask(__name__)
fa = FontAwesome(app)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hdwjsdtbcxsjmb:ad7e54aa4c50e5d35b3ca574c6425d33556fd84eb36df4630db55d3f6148749d@ec2-54-86-224-85.compute-1.amazonaws.com:5432/d5bmp15kn2c1hn'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import routes