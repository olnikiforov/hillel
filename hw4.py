import sqlite3

from flask import Flask, jsonify, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from faker import Faker


fake = Faker()

DATABASE = "users.db"





app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<User %r>' % self.name


@app.route("/")
def home():
    return "Welcome Home!"


@app.route("/users/all")
def users_all():
    cur = User.query.all()
    users = [
        dict(id=row.id, name=row.name, email=row.email)
        for row in cur
    ]
    db.session.commit()
    return jsonify(users)


@app.route("/users/gen")
def users_gen():
    usr = User(name=fake.name(), email=fake.email())
    db.session.add(usr)
    db.session.commit()
    return redirect(url_for('users_all'))


@app.route("/users/delete-all")
def users_del_all():
    db.session.query(User).delete()
    db.session.commit()
    return redirect(url_for('users_all'))


@app.route("/users/count")
def users_count():
    row = User.query.count()
    if row is None:
        return ValueError("Could not count users")
    return jsonify({"count": row})


@app.route("/users/add", methods=['GET', 'POST'])
def users_add():
    if request.method == "GET":
        return render_template("user_add.html")
    else:
        name = request.form["user_name"]
        email = request.form["email"]
    usr = User(name=name,email=email)
    db.session.add(usr)
    db.session.commit()
    return redirect(url_for('users_all'))

