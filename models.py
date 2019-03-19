import datetime
from setup import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(member_id):
    return Member.query.get(int(member_id))


class Member(db.Model, UserMixin):
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    profile_pic = db.Column(db.String(30), nullable=False, default='op_profile_default.png')
    movies = db.relationship('Movie', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.movies}')"


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"Genre('{self.name}')"


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.datetime.now)
    release_year = db.Column(db.Integer, nullable=False)
    director = db.Column(db.String(30), nullable=False)
    duration_hrs = db.Column(db.Integer, nullable=False)
    duration_mins = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    storyline = db.Column(db.Text, nullable=False)
    poster = db.Column(db.String(20), nullable=False,
                       default='movie_poster_default.jpg')
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    genre = db.relationship('Genre')
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    member = db.relationship('Member')

    def __repr__(self):
        return ("Movie"
                f"('{self.title}',"
                f" '{self.director}',"
                f" '{self.rate}',"
                f" '{self.duration_hrs}:{self.duration_mins}',"
                f" '{self.release_year}',"
                f" '{self.genre.name}'"
                f" '{self.author.username}'"
                f" '{self.date_posted.strftime('%Y-%m-%d %I:%M%p')}')")
