from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.static_folder = 'assets'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')


if __name__ == '__main__':
    app.run(debug=True,port=5001);