from app import app
from flask import render_template
from data import getParsedData

template_data = getParsedData()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', data=template_data)

@app.route('/refresh-data')
def refresh():
    global template_data 
    template_data = getParsedData()
    return "Refreshed data!"