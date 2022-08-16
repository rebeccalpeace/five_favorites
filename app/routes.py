from app import app


@app.route('/')
def index():
    return 'Hello world.'

@app.route('/five_favorites')
def favorites():
    return 'list of five favorites'