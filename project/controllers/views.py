from project import app
from flask import render_template,request,redirect
from project.models import *
@app.route('/')
def start():
    allEmp = databaseConnect.getAllEmp()
    # print(len(allEmp))
    return render_template('index.html',data=allEmp)
@app.route("/delete")
def delete():
    id = request.args.get("id")
    databaseConnect.deleteEmp(id)
    return redirect('/')
@app.route("/insert",methods=['POST','GET'])
def insert():
    if request.method == 'GET':
        return render_template('insert.html')
    elif request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        databaseConnect.insertEmp(name, phone)
        return redirect('/')
@app.route("/update",methods=['GET','POST'])
def update():
    if request.method == 'GET':
        id = request.args.get("id")
        # print(id)
        e = databaseConnect.getEmp(id)
        return render_template("update.html",data=e)
    elif request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        phone = request.form['phone']
        databaseConnect.updateEmp(id, name, phone)
        return redirect('/')
