from flask import send_file, render_template
from app import app
import os

@app.route('/libs/<filename>')
def libs(filename):
    absolute_path = os.path.dirname(__file__)
    relative_path = "static/libs/"
    return send_file(os.path.join(absolute_path, relative_path) + str(filename))

@app.route('/')
@app.route('/index')
def index():
    return render_template("base.html")
    