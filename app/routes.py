from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/five_favorites')
def favorites():
    favorites = ['Orange', 'Key Lime', 'Coconut', 'Apricot', 'Mango']
    return render_template('favorites.html', favorites=favorites)