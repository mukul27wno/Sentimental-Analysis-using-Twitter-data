from markupsafe import escape
from flask import Flask 
import os

PEOPLE_FOLDER = os.path.join('Twitter-analysis-flask', 'images')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

from routes import * 

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)