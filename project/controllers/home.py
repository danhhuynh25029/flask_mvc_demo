from project import app
from flask import render_template,request
from project.models.printer import *
@app.route('/')
def start():
    p = Printer()
    data = p.getData()
    return render_template('index.html',data=data)
