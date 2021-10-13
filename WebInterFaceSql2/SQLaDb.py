from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss
#from Data import *

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
Scss(app, static_dir='static', asset_dir='assets')

db =  SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.String(200), primary_key=True)
    user_pass = db.Column(db.String(200), nullable=False)
    user_First = db.Column(db.String(200), nullable=False)
    user_Last = db.Column(db.String(200), nullable=False)
    userData = db.relationship('UserData', backref='id', lazy=True)

class UserData(db.Model):
    __tablename__ = 'UserData'
    id = db.Column(db.String(200), primary_key=True)
    User_id = db.Column(db.String(200), db.ForeignKey('User.id'),
                          nullable=False)
    users = db.relationship('User', backref='userData', lazy=True)
    walls = db.relationship('Walls', backref='usersData', lazy=True)

class Walls(db.Model):
    __tablename__ = 'Walls'
    id = db.Column(db.String(200), primary_key=True)
    User_Data_id = db.Column(db.String(200), db.ForeignKey('UserData.id'),
                          nullable=False)
    usersData = db.relationship('UserData', backref='walls', lazy=True)
    walls = db.relationship('Wall', backref='wall', lazy=True)

class Wall(db.Model):
    __tablename__ = 'Wall'
    id = db.Column(db.String(200), primary_key=True)
    Walls_id = db.Column(db.String(200), db.ForeignKey('Walls.id'),
                          nullable=False)
    walls = db.relationship('UserData', backref='Walls', lazy=True)
    wall = db.relationship('Nodes', backref='nodes', lazy=True)

class Nodes(db.Model):
    __tablename__ = 'Nodes'
    id = db.Column(db.String(200), primary_key=True)
    Wall_id = db.Column(db.String(200), db.ForeignKey('Wall.id'),
                          nullable=False)
    wall = db.relationship('Wall', backref='wall', lazy=True)
    nodes = db.relationship('Node', backref='node', lazy=True)   
    
class Node(db.Model):
    __tablename__ = 'Node'
    id = db.Column(db.String(200), primary_key=True)
    Nodes_id = db.Column(db.String(200), db.ForeignKey('Nodes.id'),
                          nullable=False)
    nodes = db.relationship('Nodes', backref='nodes', lazy=True)
    node = db.relationship('UnitData', backref='node', lazy=True)

class UnitData(db.Model):
    __tablename__ = 'UnitData'
    id = db.Column(db.String(200), primary_key=True)
    FX = db.Column(db.Integer, nullable=True)
    FY = db.Column(db.Integer, nullable=True)
    FZ = db.Column(db.Integer, nullable=True)
    FTX = db.Column(db.Integer, nullable=True)
    FTY = db.Column(db.Integer, nullable=True)
    Node_id = db.Column(db.Integer, db.ForeignKey('Node.id'),
                          nullable=False)
    node = db.relationship('Node', backref='node', lazy=True)

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form.get('createBut') == 'Create Account':
            return render_template('createNewUser.html', login=login)
        elif request.form.get('logBut') == 'Login':
            username = request.form['username']
            password = request.form['password']
            user = get_user(username)
            if (check_Password(password, user)):
                return render_template('userHomePage.html', login=login)
            else:
                error = 'Invalid Password. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logmod', methods=['GET', 'POST'])
def logmod():
    return render_template('logmod.html')
    
# Route for handling the login page logic
@app.route('/createNewUser', methods=['GET', 'POST'])
def createNewUser():
    error = None
    if request.method == 'POST':
        if request.form.get('createBut') == 'Create Account':
            username = request.form['username']
            if(not get_user(username)):
                pass
                password = request.form['password']
                confirm = request.form['confirmPassword']
                if (password == confirm):
                    first = request.form['name_First']
                    last = request.form['name_Last']
                    user = User(id = username, user_pass = password,
                                user_First = first, user_Last = last, userData = "TempIndex")
                    return render_template('userHomePage.html', createNewUser=createNewUser)
                else: 
                    error = 'Passwords do not match'
                    return render_template('createNewUser.html', error=error)
            else:
                error = 'UserName Already Exist. Please try again.'
                return render_template('createNewUser.html', error=error)


def get_user(name):
    try:
        user = User.query.filter_by(id=name).first()
        return user
    except TypeError:#not actually type error need to figure out which error it actually is
        pass

def check_Password(password,user):    
    if (user.user_pass == password):
        return True
    else:
        return False

@app.route('/userHomePage', methods=['GET', 'POST'])
def homepage():
    return render_template('userHomePage.html')
    
if __name__ == "__main__":
    app.run(debug=True)