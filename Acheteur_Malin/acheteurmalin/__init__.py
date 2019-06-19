from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from acheteurmalin.config import Config
#from pymongo import MongoClient

"""
client = MongoClient('cluster@-e8trm.mongodb.net',
			username='gomgom',
			password='gomgom01',
			authSource='test',
			authMechanism='SCRAM-SHA-256')"""

mongo = PyMongo()
bcrypt = Bcrypt()


#client = MongoClient("mongodb+srv://gomgom:gomgom01@cluster0-e8trm.mongodb.net/test?retryWrites=true&w=majority")

def create_app(config_class=Config):

	app = Flask(__name__)
	app.config.from_object(Config)

	mongo.init_app(app)
	bcrypt.init_app(app)
		
	from acheteurmalin.categories.routes import categories
	from acheteurmalin.main.routes import main		

	app.register_blueprint(categories)
	app.register_blueprint(main)

	return app