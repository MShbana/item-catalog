from flask import render_template
from setup import app


# Dummy Data #
genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary'	, 'Drama', 'Family', 'Fantasy', 'Game Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport'	, 'Superhero', 'Talk Show', 'Thriller', 'War', 'Western']
movies = ['Home Alone', 'The Purge', 'Rush Hour', "The God Father", "Eternal Sunshine of the Spottless Mind"]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', genres=genres, movies=movies)
