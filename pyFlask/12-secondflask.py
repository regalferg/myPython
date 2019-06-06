#!/usr/bin/python3

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello admin!'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello {} Guest'.format(guest)

@app.route('/user/<name>')
def hello_user(name):
    if name.lower() == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))

if __name__ =='__main__':
    app.run(port=5006)
