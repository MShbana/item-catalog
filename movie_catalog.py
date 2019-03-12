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
    genre = Genre.query.get(int(genre_id))
    movies = Movie.query.filter_by(genre=genre).all()
    movies_count = Movie.query.filter_by(genre=genre).count()
    return render_template('genre.html',
                           genres=genres,
                           genre=genre,
                           movies=movies,
                           movies_count=movies_count,
                           title=genre.name)


@app.route('/genre/<int:genre_id>/movie/<int:movie_id>')
def movie(genre_id, movie_id):
    movie = Movie.query.get(int(movie_id))
    return render_template('movie.html', movie=movie, title=movie.title)
