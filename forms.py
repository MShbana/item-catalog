import datetime
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (StringField, IntegerField, SelectField,
                     TextAreaField, SubmitField, validators)
from wtforms.validators import (InputRequired, Regexp, Length,
                                NumberRange, Optional)


class BaseMovieForm(FlaskForm):
    current_year = datetime.datetime.now().year

    dir_reg = ('^([a-zA-Z][a-zA-Z\s.-]*[a-zA-Z])$')
    dir_err = ('Director\'s name may only contain [letters, spaces, hyphens,'
               ' periods] and should begin and end with a letter.')
    h_err = 'Duartion Hours must be between 0 and 10.'
    m_err = 'Duration Minutes must be between 0 and 60.'

    director = StringField('Director',
                           render_kw={'placeholder': 'Movie Director'},
                           validators=[
                                InputRequired(),
                                Regexp(dir_reg, message=dir_err),
                                Length(min=2, max=30)])
    release_year = SelectField('Release Year',
                               coerce=int,
                               choices=[(year, year)
                                        for year in range(1877, current_year)],
                               validators=[InputRequired()])
    genre = SelectField('Genre',
                        choices=[],
                        validators=[InputRequired()])
    duration_hrs = IntegerField('hrs',
                                render_kw={'placeholder': 'Duration in Hours'},
                                validators=[
                                    InputRequired(),
                                    NumberRange(min=0, max=10, message=h_err)])
    duration_mins = IntegerField('mins',
                                 render_kw={
                                    'placeholder': 'Duration in Minutes'},
                                 validators=[
                                    InputRequired(),
                                    NumberRange(min=0, max=60, message=m_err)])
    rate = SelectField('Rate',
                       coerce=int,
                       choices=[(rate, rate) for rate in range(1, 11)],
                       default=10,
                       validators=[InputRequired()])
    poster = FileField('Poster',
                       validators=[Optional(),
                                   FileAllowed(['jpg', 'jpeg', 'png'])])
    storyline = TextAreaField('Storyline',
                              validators=[InputRequired(),
                                          Length(min=50, max=700)])


class NewMovieForm(BaseMovieForm):
    title_reg = '^([a-zA-Z0-9][a-zA-Z0-9\s:.\'\"-?]*)$'
    title_err = ('Title may only contain alphanumeric characters,'
                 ' and should begin with a letter'
                 ' or a number')

    title = StringField('Title',
                        render_kw={'placeholder': 'Movie Title'},
                        validators=[
                            InputRequired(),
                            Regexp(title_reg, message=title_err),
                            Length(min=2, max=50)])
    submit = SubmitField('Post')


class UpdateMovieForm(BaseMovieForm):
    title_reg = '^([a-zA-Z0-9][a-zA-Z0-9\s:.\'\"-?]*)$'
    title_err = ('Title may only contain alphanumeric characters,'
                 ' and should begin with a letter'
                 ' or a number')

    title = StringField('Title',
                        render_kw={'readonly': True},
                        validators=[
                            InputRequired(),
                            Regexp(title_reg, message=title_err),
                            Length(min=2, max=50)])
    genre = SelectField('Genre',
                        render_kw={'readonly': True},
                        validators=[InputRequired()])
    submit = SubmitField('Update')
