from flask import Flask



app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world.'

@app.route('/five_favorites')
def favorites():
    return 'list of five favorites'