import datetime
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (StringField, IntegerField, SelectField, 
                     TextAreaField, SubmitField,validators)
from wtforms.validators import (InputRequired, Regexp, Length,
                                NumberRange, Optional)


class BaseMovieForm(FlaskForm):
    current_year = datetime.datetime.now().year

    director = StringField('Director',
                            render_kw={
                                'placeholder': 'Movie Director'
                            },
                            validators=[
                                InputRequired(),
                                Regexp('^([a-zA-Z][a-zA-Z\s.-]*[a-zA-Z])$', message='Director name may only contain [letters, spaces, hyphens, periods] and should begin and end with a letter.'),
                                Length(min=2, max=30)
                            ]
    )
    release_year = SelectField('Release Year',
                               coerce=int,
                               choices=[(year, year) for year in range(1877, current_year)],
                               validators=[
                                    InputRequired()
                               ]
    )
    genre = SelectField('Genre',
                        choices=[],
                        validators=[
                            InputRequired()
                        ]
    )
    duration_hrs = IntegerField('hrs',
                                render_kw={
                                    'placeholder': 'Duration in Hours'
                                },
                                validators=[
                                    InputRequired(),
                                    NumberRange(min=0, max=10, message='Duartion Hours must be between 0 and 10.')
                                ]
    )
    duration_mins = IntegerField('mins',
                                 render_kw={
                                     'placeholder': 'Duration in Minutes'
                                 },
                                 validators=[
                                     InputRequired(),
                                     NumberRange(min=0, max=60, message='Duration Minutes must be between 0 and 60.')
                                 ]
    )
    rate = SelectField('Rate',
                       coerce=int,
                       choices=[(rate, rate) for rate in range(1, 11)],
                       default=10,
                       validators=[
                           InputRequired()
                       ]
    )
    poster = FileField('Poster',
                       validators=[
                           Optional(),
                           FileAllowed(['jpg', 'jpeg', 'png'])
                       ]
    )
    storyline = TextAreaField('Storyline',
                              validators=[
                                  InputRequired(),
                                  Length(min=50, max=1000)
                              ]
    )
    post = SubmitField('Post')


class NewMovieForm(BaseMovieForm):
    title = StringField('Title',
                        render_kw={
                            'placeholder': 'Movie Title'
                        },
                        validators=[
                            InputRequired(),
                            Regexp('^([a-zA-Z0-9][a-zA-Z0-9\s:.-]*[a-zA-Z0-9])$', message='Title may only contain [letters, numbers, hyphens, periods, colons, spaces] and should begin and end with a letter or number.'),
                            Length(min=2, max=50)
                        ]
    )

class UpdateMovieForm(BaseMovieForm):
    title = StringField('Title',
                        render_kw={
                            'readonly': True
                        },
                        validators=[
                            InputRequired(),
                            Regexp('^([a-zA-Z0-9][a-zA-Z0-9\s:.-]*[a-zA-Z0-9])$', message='Title may only contain [letters, numbers, hyphens, periods, colons, spaces] and should begin and end with a letter or number.'),
                            Length(min=2, max=50)
                        ]
    )
    genre = SelectField('Genre',
                        render_kw={
                            'readonly':True
                        },
                        validators=[
                            InputRequired()
                        ]
    )
