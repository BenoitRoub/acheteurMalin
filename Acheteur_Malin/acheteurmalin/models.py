"""
from datetime import datetime
from acheteurmalin import db
#class Categorie(db.Model):			
#	id = db.Column(db.Integer, primary_key=True)
#	nom = db.Column(db.String(50), nullable=False)
#	objet = db.relationship('Objet', backref='objet', lazy=True)

class Objet(db.Document):
	#id = db.IntField(primary_key=True)
	nom = db.StringField(50, nullable=False) 
	image_file = db.StringField(20, nullable=False)
	affiliation = db.StringField(50, nullable=False)
	commentaire = db.StringField(50, nullable=False)
	#categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'), nullable=False)
	categorie = db.StringField(50, nullable=False)

	def __repr__(self):
		return f"User('{self.nom}','{self.image_file}','{self.affiliation}','{self.commentaire}', '{self.categorie}')"
"""
"""
class Objet(db.Document):
	id = db.Column(db.Integer, primary_key=True)
	nom = db.Column(db.String(50), nullable=False)
	image_file = db.Column(db.String(20), default='default.jpg', nullable=False)
	affiliation = db.Column(db.String(50), nullable=False)
	commentaire = db.Column(db.String(50), nullable=False)
	#categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'), nullable=False)
	categorie = db.Column(db.String(50), nullable=False)

	def __repr__(self):
		return f"User('{self.nom}','{self.image_file}','{self.affiliation}','{self.commentaire}', '{self.categorie}')"

"""
