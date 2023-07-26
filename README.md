# Htmx demo: adding nice UI behaviors to a simple Django movie app.

This repo is for a 2-part [PDM](https://pybit.es/catalogue/the-pdm-program/) Code Clinic I gave implementing various htmx effects.

## Get it running 💪

```
$ git clone git@github.com:bbelderbos/htmx-demo.git
$ cd htmx-demo
$ python3 -m venv venv
$ source venv/bin/activate

(venv) $ pip install -r requirements.txt

# create sqlite DB and run Django migrations
(venv) $ python manage.py migrate
...
  Applying sessions.0001_initial... OK

(venv) $ python manage.py import_movies data/movie_data.csv
...
978 movies imported

(venv) $ python manage.py runserver
```

Browse to http://locahost:8000 - enjoy 😎

Here is a quick animation of the htmx examples we implemented:

Doc links (in order of demo animation):
- [Infinite scroll](https://htmx.org/examples/infinite-scroll/)
- [Delete Row](https://htmx.org/examples/delete-row/)
- [Click to edit](https://htmx.org/examples/click-to-edit/)
- [Active Search](https://htmx.org/examples/active-search/)

Related htmx Pybites YouTube videos:
- [How to make an infinite scroll of YouTube videos using FastAPI, SQLModel and htmx](https://www.youtube.com/watch?v=5uOCUkJU-4Q)
- [Plotting database tables using SQLAlchemy automap, Flask, htmx and Chart.js](https://www.youtube.com/watch?v=EbKeZkobGbA) (here I implemented [Cascading Selects](https://htmx.org/examples/value-select/))

For more ideas [open an issue](https://github.com/bbelderbos/htmx-demo/issues) and feel free to contribute [opening a pull request](https://github.com/bbelderbos/htmx-demo/pulls) 🙏

- [Bob](https://github.com/bbelderbos).
