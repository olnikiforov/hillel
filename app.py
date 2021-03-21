from flask import Flask
from faker import Faker
from random import choice
import string
import requests

fake = Faker()

app = Flask(__name__)


@app.route('/')
def main():
    return 'Welcome!'
def generate():
    return fake.name() + fake.email()+"<br>"

@app.route('/users/generate')
@app.route('/users/generate/<int:amount>')
def users_generating(amount=20)->str:
    res = ""
    for _ in range(amount):
        res+= generate()
    return res

def password(len):
    res=""
    for _ in range(len):
        res+= choice(string.printable)
    return res

@app.route('/password/generate')
@app.route('/password/generate/<int:len>')
def password_generating(len=8)->str:
    res = password(len)
    return "Your password: "+ res

@app.route('/astro')
def astro() -> str:
    data = requests.get("http://api.open-notify.org/astros.json", json={"key": "value"}).json()
    return "Astronauts amount="+str(data['number'])

if __name__ == '__main__':
    app.run()
