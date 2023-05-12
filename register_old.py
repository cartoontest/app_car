from flask import Flask, request, redirect, url_for
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    # Add code here to handle the form submission
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return 'Registration sssssuccessful'

if __name__ == '__main__':
    app.run(debug=True)

