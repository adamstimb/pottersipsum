from flask import render_template
from app import app

from .potters import generate_potters

@app.route('/')
def home():
    return render_template('home.html', paragraphs=generate_potters())
