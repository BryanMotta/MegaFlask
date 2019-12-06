from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bryan'}
    posts = [
        {
            'author' : { 'username': 'Igor' },
            'body': 'Bad ass Motherfucker'
        },
        {
            'author': { 'username':'Felipinho' },
            'body': 'Little Bad ass Motherfucker'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)
