from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
#from acheteurmalin.models import Objet #, Categories
from flask_login import current_user

class EnregistrerForm(FlaskForm):
	nom = StringField('Nom', 
					validators=[DataRequired(), Length(min=2, max=20)])
	categorie = StringField('Categorie', 
					validators=[DataRequired(), Length(min=2, max=20)])
	image_file = StringField('Image_file', 
					validators=[DataRequired()])
	affiliation = StringField('Affiliation', 
					validators=[DataRequired(),])
	commentaire = StringField('Commentaire', 
					validators=[DataRequired(),])
	submit = SubmitField('Enregistrer')


"""class CategorieForm(FlaskForm):
	nom = StringField('Nom', 
					validators=[DataRequired(), Length(min=2, max=20)])
	submit = SubmitField('Enregistrer')"""