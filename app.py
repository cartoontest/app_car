
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
app = Flask(__name__)
app.secret_key = 'mysecretkey'  # set a secret key for session management

# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# create user model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('index.html', username=username)
    else:
        return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # save the user's data to the database
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        session['username'] = username  # add the user to the session
        return redirect(url_for('success'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # check if the user exists in the database
        user = User.query.filter_by(username=username, password=password).first()
        if user is not None:
            session['username'] = username  # add the user to the session
            session['logged_in'] = True
            return redirect('/')
        else:
            return render_template('login.html', message='Invalid username or password')
    return render_template('login.html')

@app.route('/home')
def home():
    username = get_current_user()  # replace with your own function to get the current user's username
    return render_template('home.html', username=username)

@app.route('/success')
def success():
    username = session['username']  # retrieve the user from the session
    return f"Welcome {username}!"

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

@app.route('/search', methods=['POST'])
def search():
    location = request.form['location']
    date = request.form['date']
    time = request.form['time']
    results = search_function(location, date, time) # call the search function
    return render_template('search_results.html', results=results)

@app.route('/reservation')
def reservation():
    return render_template('reservation.html')

if __name__ == '__main__':
    app.run(port=2000)
