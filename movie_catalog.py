import utils
from flask import render_template, redirect, request, url_for, flash
from models import db, Movie, Genre
from setup import app


@app.route('/')
@app.route('/home')
def home():
    '''Show all genres in the sidebar and the five latest movies.'''

    # Used to show all genres in the sidebar.
    genres = Genre.query.all()
    movies = Movie.query.order_by(Movie.date_posted.desc()).limit(5).all()
    return render_template('home.html', genres=genres, movies=movies)


@app.route('/genre/<int:genre_id>/movies')
def genre(genre_id):
    '''Display the selected genre and its movies.'''

    # Used to show all genres in the sidebar.
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
    '''Display the selected movie page.'''

    movie = Movie.query.get(int(movie_id))
    return render_template('movie.html', movie=movie, title=movie.title)


@app.route('/movie/new', methods=['GET', 'POST'])
def create_movie():
    '''Create a new movie and commit it to the database.'''

    # Used in the form's "Select Genre" field.
    genres = Genre.query.all()
    if request.method == 'POST':
        genre = Genre.query.filter_by(name=request.form['genre']).first()
        movie = Movie(title=request.form['title'],
                      director=request.form['director'],
                      release_year=request.form['release-year'],
                      genre=genre,
                      duration_hrs=request.form['duration-hrs'],
                      duration_mins=request.form['duration-mins'],
                      rate=request.form['rate'],
                      storyline=request.form['storyline'])
        # check if the user uploaded an image, if not use the default.
        if request.files.get('poster'):
            uploaded_poster_img = request.files['poster']
            stored_poster_fn = utils.save_image(uploaded_poster_img,
                                                'static/imgs/movie_pics')
            movie.poster = stored_poster_fn
        db.session.add(movie)
        db.session.commit()
        flash(f'You have successfully added the movie "{movie.title}"'
              f' to the "{movie.genre.name}" genre!', category='success')
        return redirect(url_for('movie', genre_id=genre.id, movie_id=movie.id))

    return render_template('create_edit_movie.html', genres=genres)
