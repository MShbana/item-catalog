# Item Catalog
Second required project for the [Full Stack Web Developer Nanodegree][link_1].

## Project Overview
>In this project, you will be developing a web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Authenticated users should have the ability to post, edit, and delete their own items.
>You will be creating this project essentially from scratch, no templates have been provided for you. This means that you have free reign over the HTML, the CSS, and the files that include the application itself utilizing Flask.

1. I have chosen **Movies** to be the site's **Items**, and **Genres** to be the site's **Categories**.
2. **Third Party Authentication and Authorization (OAuth2.0):** Gmail Sign in ([httplib2][link_2], [requests][link_3]) + [Flask-Login][link_4].
3. **Front-End:** HTML, CSS, [Boostrap][link_5], JS(Jquery).
4. **ORM for the database:** [SQLAlchemy][link_6], [Flask-SQLAlchemy][link_7].
5. **Templating engine:** [Python's Jinja2][link_8].
6. **Server-side Form Validation:** [WTForms][link_9] and [Flask-WTF][link_10] Validators.
7. **Storing movie posters:** [Pillow][link_11].

---

## Prerequisites and Requirements
1. **Front end:**
    - HTML
    - CSS
    - Bootstrap
    - JS(JQuery)
2. **Back end (Python3.6.x):**
    - Flask
    - SQLAlchemy
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

## Configuration and Installation
1. `git clone https://github.com/MShbana/item-catalog.git movie-catalog` to **clone** the project in a new directory, named `movie-catalog`.
2. To create a new **Python's virtual environment** with all the required project dependencies, run the following commands in the terminal (With the cloned directory `movie-catalog` as the **Current Working Directory**):
    - `virtualenv -p /usr/bin/python3 movie_catalog_env` to create a new *Python3* virtual environment.
    - `source movie_catalog_env/bin/activate` to activate the virtual environment.
    - `pip install -r requirements.txt` to install the required libararies.

3. Create the app's **SECRET_KEY**:
    - Open the *Python* interpreter.
    - `import os`.
    - `os.urandom(24)` will result in a random 24-character string.
    - Run `export SECRET_KEY='<Insert the string that os.urandom(24) has generated here>'` inside one of the following:
        - The *terminal*.
        > Will only work for the terminal session in which it was exported, i.e., you will need to export it each time you run the project in a new terminal.

        - The *.bashrc* file in the home directory.
        > Will work in any terminal session.

4. `export SQLALCHEMY_DATABASE_URI='sqlite:///site.db'`, which is the database that will be genrated by the `models.py` script, either in the *terminal* or the *.bashrc* file &mdash; same as **3**.
5. `export FLASK_APP=movie_catalog.py`, either in the *terminal* or the *.bashrc* file &mdash; same as **3**.

6. **Third Party Authentication and Authorization using OAuth2.0** (Obtaining client_id and client_secret):

    - Use your Google Account to login to the [Google Developer's Console][link_12] and click on **CREATE**:

    ![Alt text][readme_img1]    

    - Choose the **Project name**:

    ![Alt text][readme_img2]

    - From the **Create Credentials** menu, choose **OAuth client ID**:

    ![Alt text][readme_img3]

    - Click on the **Configure consent screen** button on the right:

    ![Alt text][readme_img4]

    - Enter the **Application name** and save:

    ![Alt text][readme_img5]

    - Choose **Web application** as the **Application type**, and add the **URIs**: `http://localhost:5000` and `http://127.0.0.1:5000` to both the **Authorized JavaScript origins** and **Authorized redirect URIs** fields:

    ![Alt text][readme_img6]

    - A new window will pop up with your **Client ID**, and **Client Secret**:

    ![Alt text][readme_img7]

    - Choose the Movie Catlog app to get the JSON file that contains the **Client ID** and **Client Secret**:

    ![Alt text][readme_img8]

    - Click on **Download JSON**:

    ![Alt text][readme_img9]

    - Rename the downloaded **JSON** file as: **client_secret.json** and move it to the app's directory.

    - Insert the **client_id** that you have obtained above into the **templates/login.html** file.

7. Run `python add_genres.py` in the *terminal*; to add the available movies' genres.

8. You can add some test movies by running `python add_movies.py` in the *terminal*. However, to do so, you will need to log in with at least 3 different **Gmail accounts** whose to-be-stored **id**'s will be used in the **add_movies.py** script. This will make sure that each of the three **authenticated users** has some movies, which no one else can update/delete.

9. `flask run` to run the app on the default port **5000**, or `flask run -p <port_number>` to run the app on a different port.
    > Remember to update **Authorized JavaScript origins** and **Authorized redirect URIs** fields in the Google Sign in App Configuration, if you choose to use any port number other than 5000.

10. In the browser, open the app by opening the URI `http://localhost:<port_number>` or `http://127.0.0.1:<port_number>`

---

## Screenshots of the Working Project

1. **Home Page** [Logged in as *Dwight K.Schrute*]

    ![Alt text][site_img1]


2. **Home Page Genres** [Logged in as *Dwight K.Schrute*]

    ![Alt text][site_img2]

3. **Home Page &mdash; 2 different authenticated users**

    ![Alt text][site_img3]

4. **Fantasy Genre Page** [Logged in as *Dwight K. Schrute*]

    ![Alt text][site_img4]

5. **Authenticated User's Movie List** [Logged in as *Dwight k.Schrute*]

    ![Alt text][site_img5]

6. **Not the authenticated User's Movie List** [Logged in as *Dwight Schrute*]

    ![Alt text][site_img6]

7. **Home Page** [Logged out]

    ![Alt text][site_img7]

8. **New Movie Form** [Logged in as *Dwight Schrute*]

    ![Alt text][site_img8]

9. **New Movie Form Backend Validation** [Logged in as *Dwight Schrute*]

    ![Alt text][site_img9]

10. **Update Movie Form** [Logged in as *Dwight Schrute*]

    ![Alt text][site_img10]

---

## Screenshots of the JSON API endpoints' outputs:

1. `curl http://localhost:5000/API/genres.json` returns all movie genres

    ![Alt text][genres_img]

2. `curl http://localhost:5000/API/genre/<genre_id>.json` returns the genre's name and movies

    ![Alt text][genre_img]

3. `curl http://localhost:5000/API/movies.json` reutrns
all movies

    ![Alt text][movies_img]


4. `curl http://localhost:5000/API/genre/<genre_id>/movie/<movie_id>.json` reutnrs movie details

    ![Alt text][movie_img]

5. `curl http://localhost:5000/API/users.json` returns all users

    ![Alt text][users_img]

6. `curl http://localhost:5000/API/user/<user_id>.json` returns user's information

    ![Alt text][user_img]




[//]:  # (Links and images relative paths)

[link_1]: <https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004>
[link_2]: <https://httplib2.readthedocs.io/en/latest/>
[link_3]: <http://docs.python-requests.org/en/master/>
[link_4]: <https://flask-login.readthedocs.io/en/latest/>
[link_5]: <https://getbootstrap.com/>
[link_6]: <https://www.sqlalchemy.org/>
[link_7]: <http://flask-sqlalchemy.pocoo.org/2.3/>
[link_8]: <http://jinja.pocoo.org/docs/2.10/>
[link_9]: <https://wtforms.readthedocs.io/en/stable/>
[link_10]: <https://flask-wtf.readthedocs.io/en/stable/>
[link_11]: <https://pillow.readthedocs.io/en/stable/>
[link_12]: <https://console.developers.google.com/apis/credentials>
[readme_img1]: <./static/imgs/screenshots/google_login/1.png?raw=true>
[readme_img2]: <./static/imgs/screenshots/google_login/2.png?raw=true>
[readme_img3]: <./static/imgs/screenshots/google_login/3.png?raw=true>
[readme_img4]: <./static/imgs/screenshots/google_login/4.png?raw=true>
[readme_img5]: <./static/imgs/screenshots/google_login/5.png?raw=true>
[readme_img6]: <./static/imgs/screenshots/google_login/6.png?raw=true>
[readme_img7]: <./static/imgs/screenshots/google_login/7.png?raw=true>
[readme_img8]: <./static/imgs/screenshots/google_login/8.png?raw=true>
[readme_img9]: <./static/imgs/screenshots/google_login/9.png?raw=true>
[site_img1]: <./static/imgs/screenshots/site/1.png?raw=true>
[site_img2]: <./static/imgs/screenshots/site/2.png?raw=true>
[site_img3]: <./static/imgs/screenshots/site/3.png?raw=true>
[site_img4]: <./static/imgs/screenshots/site/4.png?raw=true>
[site_img5]: <./static/imgs/screenshots/site/5.png?raw=true>
[site_img6]: <./static/imgs/screenshots/site/6.png?raw=true>
[site_img7]: <./static/imgs/screenshots/site/7.png?raw=true>
[site_img8]: <./static/imgs/screenshots/site/8.png?raw=true>
[site_img9]: <./static/imgs/screenshots/site/9.png?raw=true>
[site_img10]: <./static/imgs/screenshots/site/10.png?raw=true>
[genres_img]: <./static/imgs/screenshots/apis/genres.png?raw=true>
[genre_img]: <./static/imgs/screenshots/apis/genre.png?raw=true>
[movies_img]: <./static/imgs/screenshots/apis/movies.png?raw=true>
[movie_img]: <./static/imgs/screenshots/apis/movie.png?raw=true>
[users_img]: <./static/imgs/screenshots/apis/users.png?raw=true>
[user_img]: <./static/imgs/screenshots/apis/user.png?raw=true>
