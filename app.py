🟢 1. Flask Introduction (Basics)

🔹 Flask Kya Hai?
Flask ek lightweight Python web framework hai jo web applications aur APIs banane ke liye use hota hai.

Installation
pip install flask

🔹 First Flask App
app.py

from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)



🟢 2. Routing (Multiple URLs Handle Karna)

@app.route('/about')
def about():
    return "About Page"

@app.route('/user/<name>')
def user(name):
    return f"Hello {name}"




🟢 3. Forms Handling (GET & POST)
@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form['name']
        return f"Welcome {name}"
    return '''
        <form method="post">
            <input type="text" name="name">
            <input type="submit">
        </form>
    '''


🟢 4. Database Integration (SQLite)

import sqlite3
conn = sqlite3.connect("database.db")
conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
conn.execute("INSERT INTO users (name) VALUES ('Aman')")
conn.commit()
conn.close()

Flask Integration
@app.route('/users')
def users():
    conn = sqlite3.connect("database.db")
    data = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return str(data)


🟢 5. Flask with SQLAlchemy (Professional Way)

Install:
pip install flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

@app.route('/add/<name>')
def add(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return "User Added"




🟢 6. Authentication (Login System Basic)

Install:
pip install flask-login
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)



🟢 7. REST API Development

from flask import jsonify
@app.route('/api')
def api():
    return jsonify({"name": "Aman", "age": 22})



🟢 8. File Upload

from flask import request
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(file.filename)
    return "File Uploaded"




🟢 9. Flask + JWT Authentication (Advanced API Security)

Install:
pip install flask-jwt-extended
Basic Example:
from flask_jwt_extended import JWTManager, create_access_token

app.config["JWT_SECRET_KEY"] = "secret"
jwt = JWTManager(app)

@app.route('/login', methods=["POST"])
def login():
    token = create_access_token(identity="admin")
    return {"token": token}



🟢 10. Error Handling

@app.errorhandler(404)
def not_found(e):
    return "Page Not Found", 404


🟢 11. Deployment (Production)

Gunicorn
Nginx
Docker
Example:
gunicorn app:app


🟢 12. Route.py

from flask import Blueprint
auth = Blueprint('auth', __name__)
@auth.route('/login')
def login():
    return "Login Page"

🟢 13. index.html

{% comment %} <h1>Hello {{ name }}</h1> {% endcomment %}
