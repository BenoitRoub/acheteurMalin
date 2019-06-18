from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from acheteurmalin.config import Config


mongo = PyMongo()
bcrypt = Bcrypt()




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