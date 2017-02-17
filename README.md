# Example RaspberryPi webserver using Python and Flask

To both poll and control GPIO pins on a RPI with ERM, you will need to create and run
a web app. One of the easiest langauges and libraries to do this with is Python and the Flask library.

Flask Quickstart - 
http://flask.pocoo.org/docs/0.12/quickstart/

## Create virtual env

```virtualenv -p python3 venv```

## Install Flask

```pip install flask```

## Run a server.py in debug mode

```FLASK_APP=server.py FLASK_DEBUG=1 flask run --host=0.0.0.0```


## Running in "production"
You probably do not want to use the built-in dev server when running in production.
Instead, you can use either Gevent for event based processing or Gunicorn to use subprocesses.

http://flask.pocoo.org/docs/0.12/deploying/wsgi-standalone/

### Gevent

```pip install gevent```

The code is already set up to use Gevent, so just run the server.py as a standalone app

```python server.py```