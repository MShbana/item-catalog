from flask import render_template
from models import db, Movie, Genre
from setup import app


@app.route('/')
@app.route('/home')
def home():
    genres = Genre.query.all()
    movies = Movie.query.order_by(Movie.date_posted.desc()).limit(5).all()
    return render_template('home.html', genres=genres, movies=movies)
