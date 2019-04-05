from flask import Flask, render_template, request
import requests
import os
import sys
import urllib3
import pandas as pd

app = Flask(__name__)

#UPLOAD_FOLDER = "/Users/danielruales/Documents/aaaProjects/DogBreedPython/static/"
UPLOAD_FOLDER = os.getcwd() + "/static/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
	return render_template('base.html')

if __name__ == '__main__':
	app.debug = True
	app.run()