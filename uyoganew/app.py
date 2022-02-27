import string
from flask import Flask, Response, request, render_template, send_from_directory, redirect
from transform import transform
from load import init
import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, Response, request
import cv2
import time
import os
import numpy as np
from threading import Thread
import random

model,labels = init()
labels[0] = "downwards dog"
labels[-1] = "warrior"
print(labels)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WUETGFORUWJGHOWRoihwfochneru'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

'''start'''
'''end'''


ALLOWED_EXTENSIONS = {'jpg'}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'uploadedimages/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)
    
    print(destination)
    stringy, result, confidence  = transform(destination,model,labels)
    print(stringy)
    return render_template("complete.html", image_name=filename, print = stringy)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

@app.route('/friends')
def friends():
    return render_template("friends.html")


if __name__ == '__main__':
    app.run()

