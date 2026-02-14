# 🟢 1. Flask Introduction (Basics)
# 🔹 Flask Kya Hai?

# Flask ek lightweight Python web framework hai jo web applications aur APIs banane ke liye use hota hai.

# Installation
# pip install flask

# 🔹 First Flask App
# app.py
from flask import Flask, render_template,request
# 🟢 6. Flask with SQLAlchemy (Professional Way)

# Install:

# pip install flask_sqlalchemy

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

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", name="Aman")



# 🟢 4. Forms Handling (GET & POST)
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
# 5. Database Integration (SQLite)
import sqlite3

conn = sqlite3.connect("database.db")
conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
conn.execute("INSERT INTO users (name) VALUES ('Aman')")
conn.commit()
conn.close()

# Flask Integration
@app.route('/users')
def users():
    conn = sqlite3.connect("database.db")
    data = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return str(data)


# 2. Routing (Multiple URLs Handle Karna)

@app.route('/about')
def about():
    return "About Page"

@app.route('/user/<name>')
def user(name):
    return f"Hello {name}"

# Output:

# /user/aman

if __name__ == "__main__":
    app.run(debug=True)