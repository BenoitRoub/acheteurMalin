from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '4481969b34e8b98798e232ad4f10453f'
app.config['MONGO_URI'] = 'mongodb+srv://gomgom:gomgom01@cluster0-e8trm.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)



bcrypt = Bcrypt(app)


from acheteurmalin import routes	
