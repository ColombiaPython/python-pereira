from flask import render_template
from app import app, pages
import json

@app.route('/')
def home():
    with open('data/organizador.json') as data_file:    
        organizadores = json.load(data_file)
    
    return render_template('index.html', organizadores=organizadores)
