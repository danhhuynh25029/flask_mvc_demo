from project import app
from flask import render_template,request
from project.models import *
@app.route('/')
def start():
    allEmp = databaseConnect.getAllEmp()
    print(len(allEmp))
    return render_template('index.html',data=allEmp)
