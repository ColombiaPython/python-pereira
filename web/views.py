from flask import render_template
from app import app, pages
import json
import os

from settings import APP_DATA

@app.route('/')
def home():
    with open(os.path.join(APP_DATA, 'organizador.json'), encoding='utf8') as data_file:    
        organizadores = json.load(data_file)

    with open(os.path.join(APP_DATA, 'reunion.json'), encoding='utf8') as data_file:    
        reunion = json.load(data_file)
    
    return render_template('index.html', organizadores=organizadores, proximos=reunion["proximo"], anteriores=reunion["anterior"][:(6 - len(reunion["proximo"]))])

@app.route('/eventos/')
def eventos():
    with open(os.path.join(APP_DATA, 'reunion.json'), encoding='utf8') as data_file:    
        reunion = json.load(data_file)
    
    return render_template('eventos.html', proximos=reunion["proximo"], anteriores=reunion["anterior"])
