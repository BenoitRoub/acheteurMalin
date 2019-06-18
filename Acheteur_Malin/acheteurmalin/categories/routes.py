from flask import render_template, url_for, flash, redirect, request
from acheteurmalin import mongo
from acheteurmalin.main.forms import EnregistrerForm 
from PIL import Image
import secrets
import os
from flask import Blueprint, current_app

categories = Blueprint('categories', __name__)

@categories.route("/")
def accueil():
	objet=[]
	objet=mongo.db.Objet.find()
	return render_template('accueil.html', objet=objet, title='Le site de comparatif qui conseil vos achats')

@categories.route("/hightech")
def hightech():
	objet=[]
	objet=mongo.db.Objet.find({'categorie':'hightech'})
	return render_template('hightech.html', title=' conseil et comparatif achat Hightech', objet=objet)

@categories.route("/electromenager")
def electromenager():
	objet=[]
	objet=mongo.db.Objet.find({'categorie':'elecctromenager'})
	return render_template('electromenager.html', title=' conseil et comparatif achat Hightech', objet=objet)


@categories.route("/musique")
def musique():
	objet=[]
	objet=mongo.db.Objet.find({'categorie':'musique'})
	return render_template('musique.html', title=' conseil et comparatif achat Hightech', objet=objet)


@categories.route("/telephone")
def telephone():
	objet=[]
	objet=mongo.db.Objet.find({'categorie':'telephone'})
	return render_template('telephone.html', title=' conseil et comparatif achat Hightech', objet=objet)
