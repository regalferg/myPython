#!/usr/bin/python3

from flask import Flask, render_template, request,redirect,url_for
from werkzeug import secure_filename
import re
import json



app = Flask(__name__)

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods= ['POST'])
def uploader():
    if request.method == 'POST';
        mysteryfile = request.files['file']
        mysteryfile.save(secure_filename(mysteryfile.filename))
        if 'cap' in mysteryfile.filename:
            return redirect(url_for('sip', filetoparse=mysteryfile.filename))

        else:
            return 'That format is not yet support please check back soon'

@app.route('/sip/<filetoparse>')
def sip(filetoparse):
    sipjoson =[]
    with open(filetoparse) as capture:
        for line in capture:
            matchedobj = re.search(r'^sip:\+(\d+)@\[(.*)\]:?(\d+)?', line)
            if matchedobj:
                tinylist = []
                tinylist.append(matchedobj.group())
                tinylist.append(matchedobj.group(1))
                tinylist.append(matchedobj.group(2))
                tinylist.append(matchedobj.group(3))
                sipjson.append(tinylist)
         return json.dumps(sipjson)

if __name__ == '__main__':
    app.run(port=5006)

