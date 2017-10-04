from flask import render_template
from app import app, pages

@app.route('/')
def home():
    return render_template('index.html', name='alejo', age='22')
