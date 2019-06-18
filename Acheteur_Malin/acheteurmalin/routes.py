from flask import render_template, url_for, flash, redirect, request
from acheteurmalin import app, mongo
from acheteurmalin.forms import EnregistrerForm  #, CategorieForm
"""from acheteurmalin.models import Objet  #, Categorie"""
from PIL import Image
import secrets
import os



@app.route("/")
def accueil():
	objet=[]
	objet=mongo.db.Objet.find()
	return render_template('accueil.html', objet=objet, title='Le site de comparatif qui conseil vos achats')

@app.route("/hightech")
def hightech():
	objet=[]
	objet=mongo.db.Objet.find({'categorie':'hightech'})
	return render_template('hightech.html', title=' conseil et comparatif achat Hightech', objet=objet)

@app.route("/electromenager")
def electromenager():
	objet=[]
	objet=mongo.db.Objet.find({'categorie':'elecctromenager'})
	return render_template('electromenager.html', title=' conseil et comparatif achat Hightech', objet=objet)


@app.route("/musique")
def musique():
	objet=[]
	objet=mongo.db.Objet.find({'categorie':'musique'})
	return render_template('musique.html', title=' conseil et comparatif achat Hightech', objet=objet)


@app.route("/telephone")
def telephone():
	objet=[]
	objet=mongo.db.Objet.find({'categorie':'telephone'})
	return render_template('telephone.html', title=' conseil et comparatif achat Hightech', objet=objet)

@app.route("/mentionslegales")
def mentionslegales():
	return render_template('mentionslegales.html')



def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(app.root_path, 'static/objet_photo', picture_fn)
	
	output_size = (200, 200)
	i = Image.open("acheteurmalin/static/image/" + form_picture)
	i.thumbnail(output_size) 
	i.save(picture_path)
	
	path = 'static/objet_photo/'+ picture_fn

	
	return path

@app.route("/enregistrer", methods=['GET', 'POST'])
def enregistrer():
	form = EnregistrerForm()
	if form.validate_on_submit():
		if form.image_file.data:
			image_file = save_picture(form.image_file.data)
		objet = {'nom' : form.nom.data, 'image_file' : image_file , 'affiliation' : form.affiliation.data, 'commentaire': form.commentaire.data, 'categorie' : form.categorie.data}
		mongo.db.Objet.insert_one(objet)
		flash(f'L objet à été ajouté', 'success')
		return redirect(url_for('enregistrer'))
	return render_template('enregistrer.html', title='enregistrer', form=form)

"""@app.route("/enregistrercat", methods=['GET', 'POST'])
def enregistrercat():
	cform = CategorieForm()
	if cform.validate_on_submit():
		categorie = Categorie(nom = cform.nom.data)
		db.session.add(categorie)
		db.session.commit()
		flash(f'L objet à été ajouté', 'success')
		return redirect(url_for('accueil'))
	return render_template('enregistrercat.html', title='enregistrercat', cform=cform)


	db.session.add(objet)
		db.session.commit()"""