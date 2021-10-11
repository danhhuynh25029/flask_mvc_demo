import sqlite3
# from employee import *
from project.models import employee
conn = sqlite3.connect("project/database/my_database.db",check_same_thread=False)
c = conn.cursor()
# c.execute("INSERT INTO emp(name,phone) VALUES('Danh',12131313)")
def insertEmp(n:str,p:int):
    sql = "INSERT INTO emp(name,phone) VALUES ('{}',{})".format(n,p)
    c.execute(sql)
    commit_all()
def deleteEmp(id:int):
    sql = "DELETE FROM emp WHERE id ={}".format(id)
    c.execute(sql)
    commit_all()
def getAllEmp():
    sql = "SELECT * FROM emp"
    s = c.execute(sql)
    all_emp = []
    for r in s:
        e = employee.Employee(r[0], r[1], r[2])
        all_emp.append(e)
    # conn.commit()
    commit_all()
    return all_emp
def commit_all():
    conn.commit()
    conn.close()
if __name__ == "__main__":
    all_emp = getAllEmp()
    for e in all_emp:
        print(e.getId(),e.getName(),e.getPhone())
# conn.commit()
# conn.close()