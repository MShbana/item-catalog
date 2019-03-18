import utils
from flask import render_template, redirect, request, url_for, flash
from forms import NewMovieForm, UpdateMovieForm
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
    movies = Movie.query.filter_by(genre=genre)\
        .order_by(Movie.date_posted.desc()).all()
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

    form = NewMovieForm()
    form.genre.choices = [(None, 'Select Movie Genre')]
    form.genre.choices.extend([(genre.name, genre.name) for genre in genres])

    if form.validate_on_submit():
        genre = Genre.query.filter_by(name=form.genre.data).first()
        movie = Movie(title=form.title.data.title(),
                      director=form.director.data.title(),
                      release_year=form.release_year.data,
                      genre=genre,
                      duration_hrs=form.duration_hrs.data,
                      duration_mins=form.duration_mins.data,
                      rate=form.rate.data,
                      storyline=form.storyline.data)
        # check if the user uploaded an image, if not use the default.
        if request.files.get('poster'):
            uploaded_poster_img = form.poster.data
            stored_poster_fn = utils.save_image(uploaded_poster_img,
                                                'static/imgs/movie_pics')
            movie.poster = stored_poster_fn
        db.session.add(movie)
        db.session.commit()
        flash(f'You have successfully added the movie "{movie.title}"'
              f' to the "{movie.genre.name}" genre!', category='success')
        return redirect(url_for('movie', genre_id=genre.id, movie_id=movie.id))
    return render_template('create_edit_movie.html', form=form, legend='New Movie')


@app.route('/genre/<int:genre_id>/movie/<int:movie_id>/update', methods=['GET', 'POST'])
def update_movie(movie_id, genre_id):
    '''Update Movie Information and commit to the database.'''

    movie = Movie.query.get(int(movie_id))
    form= UpdateMovieForm(obj=movie)
    form.genre.choices = [(movie.genre.name, movie.genre.name)]

    if form.validate_on_submit():
        movie.director = form.director.data
        movie.release_year = form.release_year.data
        movie.duration_hrs = form.duration_hrs.data
        movie.duration_mins = form.duration_mins.data
        movie.rate = form.rate.data
        movie.storyline = form.storyline.data
        # check if the user uploaded an image, if not use the default.
        if request.files.get('poster'):
            uploaded_poster_img = form.poster.data
            stored_poster_fn = utils.save_image(uploaded_poster_img,
                                                'static/imgs/movie_pics')
            movie.poster = stored_poster_fn
        db.session.commit()
        flash(f'You have successfully update the movie "{movie.title}"!', category='success')
        return redirect(url_for('movie', genre_id=movie.genre_id, movie_id=movie.id))
    return render_template('create_edit_movie.html', form=form, legend=f'Update {movie.title}')
