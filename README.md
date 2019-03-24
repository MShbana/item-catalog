# Item Catalog
Second required project for the [Full Stack Web Developer Nanodegree][1].

## Project Overview
>In this project, you will be developing a web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Authenticated users should have the ability to post, edit, and delete their own items.
>You will be creating this project essentially from scratch, no templates have been provided for you. This means that you have free reign over the HTML, the CSS, and the files that include the application itself utilizing Flask.

1. I have chosen Movies to be the site's items, and Genres to be the site's categories.
2. Authorization: Google Sign in server ([httplib2][2], [requests][3]).
3. Authentication: Google Sign in + [Flask-login][4].
4. Front-End: HTML, CSS, [Boostrap][5], JS(Jquery).
5. ORM for the database: [SQLAlchemy][6], [Flask-SQLAlchemy][7].
6. Templating engine: [Python's Jinja2][8].
7. Back-end Form Validation: [WTForms][9] and [Flask-WTF][10] Validators.
8. Storing movie posters: [Pillow][11].

---

## Prerequesites and Requirements
1. Front end:
    - HTML
    - CSS
    - Bootstrap
    - JQuery
2. Back end (Python3.6.x):
    - Flask
    - Flask-SQLAlchemy
    - Flask-Login
    - WTForms
    - Flask-WTF
    - Jinja2
    - Pillow
    - httplib2
    - urllib3
    - requests

---



[//]:  # (Links and references)

[1]: <https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004>
[2]: <https://httplib2.readthedocs.io/en/latest/>
[3]: <http://docs.python-requests.org/en/master/>
[4]: <https://flask-login.readthedocs.io/en/latest/>
[5]: <https://getbootstrap.com/>
[6]: <https://www.sqlalchemy.org/>
[7]: <http://flask-sqlalchemy.pocoo.org/2.3/>
[8]: <http://jinja.pocoo.org/docs/2.10/>
[9]: <https://wtforms.readthedocs.io/en/stable/>
[10]: <https://flask-wtf.readthedocs.io/en/stable/>
[11]: <https://pillow.readthedocs.io/en/stable/>
[12]: <https://developers.google.com/identity/sign-in/web/sign-in>
