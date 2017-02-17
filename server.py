from gevent.wsgi import WSGIServer  # Gevent webserver

from flask import Flask
app = Flask(__name__)

# Example variable to report - can be updated based on GPIO pin
status_pressed = True

@app.route('/status')
def status():
    # Get status of GPIO pin or variable controlled by one
    # Ex. http://localhost:5000/status

    return 'pressed' if status_pressed else 'not pressed'


@app.route('/trigger/<int:pin_num>/<string:action>')
def trigger(pin_num, action):
    # Set a GPIO pin high or low where
    # Ex. http://localhost:5000/trigger/5/high

    if action == 'high':
        print('setting to high!')
    elif action == 'low':
        print('setting to low')

    return 'setting {} to {}'.format(str(pin_num), action)



# Run Gevent in production
if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()