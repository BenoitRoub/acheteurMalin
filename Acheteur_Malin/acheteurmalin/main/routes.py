from flask import render_template, url_for, flash, redirect, request
from acheteurmalin import mongo
from acheteurmalin.main.forms import EnregistrerForm 
from PIL import Image
import secrets
import os
from flask import Blueprint, current_app


main = Blueprint('main', __name__)

@main.route("/mentionslegales")
def mentionslegales():
	return render_template('mentionslegales.html')


def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(current_app.root_path, 'static/objet_photo', picture_fn)
	
	output_size = (150, 150)
	i = Image.open("acheteurmalin/static/image/" + form_picture)
	i.thumbnail(output_size) 
	i.save(picture_path)
	
	path = 'static/objet_photo/'+ picture_fn

	
	return path

@main.route("/enregistrer", methods=['GET', 'POST'])
def enregistrer():
	form = EnregistrerForm()
	if form.validate_on_submit():
		if form.image_file.data:
			image_file = save_picture(form.image_file.data)
		objet = {'nom' : form.nom.data, 'image_file' : image_file , 'affiliation' : form.affiliation.data, 'commentaire': form.commentaire.data, 'categorie' : form.categorie.data}
		mongo.db.Objet.insert_one(objet)
		flash(f'L objet à été ajouté', 'success')
		return redirect(url_for('main.enregistrer'))
	return render_template('enregistrer.html', title='enregistrer', form=form)

