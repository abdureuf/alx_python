#user/bin/python3
"""
import flask web framework
"""
from flask import Flask, render_template
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
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    create methods that return  C with text
    """
   
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    create methods that return  by default IS COOL
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    create methods that return  only integeres
    """
    return '{} is a number'.format(n)
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    by using render_templete
    """
    if isinstance(n, int):
        return render_template('number.html', number=n)
    
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if isinstance(n, int):
        """
        by using render_templete
        """
        return render_template('odd_or_even.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)