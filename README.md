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

