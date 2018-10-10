from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/index')
def index(): 
    return render_template('index.html', title='Home')

@app.route('/notebook')
def notebook(): 
    return render_template('notebook.html')
   