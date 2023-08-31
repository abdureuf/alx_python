#user/bin/python3
"""
import flask web framework
"""
from flask import Flask
# instantiate flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    create methods that return Hello HBNB!
    """
    return 'Hello HBNB!'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    create methods that return  HBNB!
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)