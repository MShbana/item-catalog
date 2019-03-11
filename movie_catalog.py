from flask import render_template
from models import db, Movie, Genre
from setup import app


@app.route('/')
@app.route('/home')
def home():
    genres = Genre.query.all()
    movies = Movie.query.order_by(Movie.date_posted.desc()).limit(5).all()
    return render_template('home.html', genres=genres, movies=movies)


@app.route('/genre/<int:genre_id>')
def genre(genre_id):
    genres = Genre.query.all()
    genre = Genre.query.filter_by(id=genre_id).first()
    movies = Movie.query.filter_by(genre=genre).all()
    return render_template('genre.html',
                           genres=genres,
                           genre=genre,
                           movies=movies,
                           title=f'{genre.name} Movies')