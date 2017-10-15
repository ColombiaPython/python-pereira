from flask import render_template
from app import app, pages
import json

@app.route('/')
def home():
    with open('data/organizador.json') as data_file:    
        organizadores = json.load(data_file)

    with open('data/reunion.json') as data_file:    
        reunion = json.load(data_file)
    
    return render_template('index.html', organizadores=organizadores, proximos=reunion["proximo"], anteriores=reunion["anterior"][:(6 - len(reunion["proximo"]))])

@app.route('/eventos/')
def eventos():
    with open('data/reunion.json') as data_file:    
        reunion = json.load(data_file)
    
    return render_template('eventos.html', anteriores=reunion["anterior"])
