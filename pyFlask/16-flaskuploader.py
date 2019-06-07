#!/usr/bin/python3

from flask import Flask, render_template, request,redirect,url_for, send_file
from werkzeug import secure_filename
import re
import json
import smtplib
from email.message import EmailMessage
#import pandas as pd
#import numpy as np
#import matplotlib as plt
import graphin

app = Flask(__name__)

@app.route('/upload')
def upload_file():
    return render_template('uploads.html')

@app.route('/uploader', methods= ['POST'])
def uploader():
    if request.method == 'POST':
        mysteryfile = request.files['file']
        mysteryfile.save(secure_filename(mysteryfile.filename))
        if 'cap' in mysteryfile.filename:
            return redirect(url_for('sip', filetoparse=mysteryfile.filename))
        elif 'xls' in mysteryfile.filename:
            return redirect(url_for('excel', filetoparse=mysteryfile.filename))

        else:
            return 'That format is not yet support please check back soon'

@app.route('/excel/<filetoparse>')
def excel(filetoparse):
    return send_file(graphin.pygraph(filetoparse), mimetype='image/png')



@app.route('/sip/<filetoparse>')
def sip(filetoparse):
    sipjson =[]
    with open(filetoparse) as capture:
        for line in capture:
            matchedobj = re.search(r'sip:\+(\d+)@\[(.*)\]:?(\d+)', line)
            if matchedobj:
                tinylist = []
                tinylist.append(matchedobj.group())
                tinylist.append(matchedobj.group(1))
                tinylist.append(matchedobj.group(2))
                tinylist.append(matchedobj.group(3))
                sipjson.append(tinylist)
        return json.dumps(sipjson)

@app.route('/emailsender')
def emailsender():
    msg = EmailMessage()
    msg['Subject'] = 'CF is not cool'
    msg['From'] = 'pythonstudent01@mail.com'
    msg['To'] = 'rzfeeserspam@gmail.com'
    msg.preamble = 'All your base are belong to us - Charles F'
    
    with open('/home/student/emailpassword.txt') as emailpass:
        myemailpass = emailpass.read().decode('utf-8').rstrip().rstrip('\n')
    mail = smtplib.SMTP('smtp.mail.com',587)
    mail.starttls()
    mail.login('pythonstudent01@mail.com', myemailpass)
    mail.sendmail('pythonstudent01@mail.com','rzfeeserspam@gmail.com', msg.as_string())
    mail.quit()
    return 'Spammity spam spam spam'



if __name__ == '__main__':
    app.run(port=5006)

