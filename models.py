from datetime import datetime
from setup import db


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
                            default=datetime.utcnow)
    release_year = db.Column(db.Integer, nullable=False,
                             default='Undetermined')
    director = db.Column(db.String(30), nullable=False, default='Anonymous')
    duration = db.Column(db.Integer, nullable=False, default='Undetermined')
    rate = db.Column(db.Integer, nullable=False)
    storyline = db.Column(db.Text, nullable=False)
    poster = db.Column(db.String(20), nullable=False,
                       default='movie_poster_default.jpg')
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    genre = db.relationship('Genre')

    def __repr__(self):
        return ("Movie"
                f"('{self.title}',"
                f" '{self.director}',"
                f" '{self.rate}',"
                f" '{self.duration}',"
                f" '{self.release_year}',"
                f" '{self.genre.name}'"
                f" '{self.date_posted}')")
