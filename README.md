### Shapely

##### Shapes as a Service!

#### Quickstart
*Assumes psql, pyenv, pip, virtualenv, and virtualenvwrapper installed.*

Clone the Repo, setup the virtualenv and install requirements
```
git clone git@github.com/mhotwagner/shapely
mkvirtualenv shapely -p $(pyenv which python3)
workon shapely
pip install -r requirements.txt
```

Make your local database and migrate the app
```
createdb shapely-local
make migrate
```

Run the tests
`make test`

Run the local server
```
make start
```

Go get some shapes!
`http://localhost:8000/shapes`
