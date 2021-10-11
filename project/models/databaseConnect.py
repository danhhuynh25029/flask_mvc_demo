import sqlite3
from project.models import employee
conn = sqlite3.connect("project/models/my_database.db",check_same_thread=False)
c = conn.cursor()
# c.execute("INSERT INTO emp(name,phone) VALUES('Danh',12131313)")
def getEmp(id:int):
    sql = "SELECT * FROM emp WHERE id={}".format(id)
    for i in c.execute(sql):
        e = employee.Employee(i[0],i[1],i[2])
        return e
def insertEmp(n:str,p:int):
    sql = "INSERT INTO emp(name,phone) VALUES ('{}',{})".format(n,p)
    c.execute(sql)
    commit_all()
def deleteEmp(id:int):
    sql = "DELETE FROM emp WHERE id ={}".format(id)
    c.execute(sql)
    commit_all()
def updateEmp(id:int,n:str,p:int):
    sql = "UPDATE emp SET name='{}',phone={} WHERE id={}".format(n,p,id)
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
    # conn.close()
if __name__ == "__main__":
    all_emp = getAllEmp()
    for e in all_emp:
        print(e.getId(),e.getName(),e.getPhone())
# conn.commit()
# conn.close()