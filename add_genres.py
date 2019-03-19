from models import Genre
from setup import db

genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film Noir', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Science Fiction', 'Short', 'Sport', 'Superhero', 'Thriller', 'War', 'Western']

for genre in genres:
    new_genre = Genre(name=genre)
    db.session.add(new_genre)
    db.session.commit()

print('Added Genres Successfully!')