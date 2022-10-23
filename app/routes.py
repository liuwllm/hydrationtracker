from flask import render_template
from app import app
from flask import url_for

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')