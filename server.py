from flask import Flask
app = Flask(__name__)

# Example variable to report - can be updated based on GPIO pin
status_pressed = True

@app.route('/status')
def status():
    # Get status of GPIO pin or variable controlled by one
    return 'pressed' if status_pressed else 'not pressed'


@app.route('/trigger/<int:pin_num>/<string:action>')
def trigger(pin_num, action):
    # Set a GPIO pin high or low where
    # Ex. http://localhost:5000/trigger/5/high

    return 'setting {} to {}'.format(str(pin_num), action)