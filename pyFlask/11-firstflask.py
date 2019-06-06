#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/")

def endoftheday():
    return "Class is nearing the end for Wednesday"
@app.route('/hello/<name>', defaults={'position':' Admin Asst'})
@app.route('/hello/<name>/<position>')
def hellostudents(name,position):
    return 'Hello {1} {0}.I am pleased to mee thee {0}'.format(name,position)
   # return 'Welcome to class...' + name



if __name__ == "__main__":
    app.run(port=5006)
