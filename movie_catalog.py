import httplib2
import json
import random
import requests
import string
import utils
from flask import (render_template, redirect, request,
                   url_for, flash, session as login_session,
                   abort, make_response)
from flask_login import login_user, logout_user, current_user, login_required
from forms import NewMovieForm, UpdateMovieForm
from models import db, Movie, Genre, User
from oauth2client.client import flow_from_clientsecrets, FlowExchangeError
from setup import app
from sqlalchemy.orm.exc import NoResultFound


CLIENT_ID = json.loads(
    open('client_secret.json', 'r').read())['web']['client_id']


@app.route('/')
@app.route('/home')
def home():
    '''Show all genres in the sidebar and the five latest movies.'''

    # Used to show all genres in the sidebar.
    genres = Genre.query.all()
    # Pass query parameter of the page number to the url.
    page = request.args.get('page', 1, type=int)
    # Show only five movies per page, then load more when page nubmer clicked.
    movies = Movie.query.order_by(Movie.date_posted.desc()).\
        paginate(per_page=5, page=page)
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
@login_required
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
                      storyline=form.storyline.data,
                      user=current_user)

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
    return render_template('create_edit_movie.html',
                           form=form, legend='New Movie', title='New Movie')


@app.route('/genre/<int:genre_id>/movie/<int:movie_id>/update',
           methods=['GET', 'POST'])
@login_required
def update_movie(movie_id, genre_id):
    '''Update Movie Information and commit to the database.'''

    movie = Movie.query.get(int(movie_id))

    if movie.author != current_user:
        abort(403)

    form = UpdateMovieForm(obj=movie)
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
        flash(f'You have successfully updated the movie "{movie.title}"!',
              category='success')
        return redirect(url_for('movie',
                                genre_id=movie.genre_id, movie_id=movie.id))
    return render_template('create_edit_movie.html',
                           form=form,
                           legend=f'Update {movie.title}',
                           title=f'Update {movie.title.title()}')


@app.route('/genre/<int:genre_id>/movie/<int:movie_id>/delete',
           methods=['GET', 'POST'])
@login_required
def delete_movie(genre_id, movie_id):
    '''Delete a movie from the database.'''

    movie = Movie.query.get(int(movie_id))

    if movie.author != current_user:
        abort(403)

    movie_title = movie.title
    movie_genre = movie.genre.name

    if request.method == 'POST':
        db.session.delete(movie)
        db.session.commit()
        flash(f'You have successfully deleted the movie "{movie_title}"'
              f' from the "{movie_genre}" genre!', category='success')
        return redirect(url_for('home'))
    return render_template('delete_movie.html',
                           movie=movie,
                           title=f'Delete {movie.title}')


@app.route('/<string:username>/<int:user_id>/movies')
def user_movies(username, user_id):
    '''Display all the movies belonging a user.'''

    user = User.query.get(int(user_id))
    movies = Movie.query.filter_by(user_id=user_id).\
        order_by(Movie.date_posted.desc()).all()
    movies_count = Movie.query.filter_by(user_id=user_id).count()
    return render_template('user_movies.html',
                           movies=movies, user=user, movies_count=movies_count)


# Create anti-forgery state token
@app.route('/login')
def google_login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    state = ''.join(
        random.choice(string.ascii_uppercase + string.digits)
        for x in range(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(
                        json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code, now compatible with Python3
    request.get_data()
    code = request.data.decode('utf-8')

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secret.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com'
           f'/oauth2/v1/tokeninfo?access_token={access_token}')
    # Submit request, parse response - Python3 compatible
    h = httplib2.Http()
    response = h.request(url, 'GET')[1]
    str_response = response.decode('utf-8')
    result = json.loads(str_response)

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists, if it doesn't make a new one
    user_id = get_user_id(login_session['email'])
    if not user_id:
        user_id = create_user(login_session)
    login_session['user_id'] = user_id
    user = User.query.get(int(user_id))
    login_user(user)

    output = f'<h1>Welcome {login_session["username"]}!</h1>'
    output += (f'<img src="{login_session["picture"]}"'
               ' style="width:300px; height: 300px;'
               ' border-radius: 150px;'
               ' -webkit-border-radius: 150px;'
               '-moz-border-radius: 150px;">')
    flash('You are now logged in as:'
          f' {login_session["username"]}!', category='success')
    return output


def create_user(login_session):
    new_user = User(username=login_session['username'], email=login_session[
                   'email'], profile_pic=login_session['picture'])
    db.session.add(new_user)
    db.session.commit()
    user = User.query.filter_by(email=login_session['email']).first()
    return user.id


def get_user_id(email):
    try:
        user = User.query.filter_by(email=email).first()
        return user.id
    except:
        return None


@app.route('/gdisconnect')
@login_required
def gdisconnect():
    logout_user()
    flash('You are now logged out.', category='warning')
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = f'https://accounts.google.com/o/oauth2/revoke?token={access_token}'
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        # Reset the user's sesson.
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        logout_user()
        return redirect(url_for('home'))
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return redirect(url_for('home'))
