from flask import Flask,render_template,request,redirect,url_for
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='K@sim@7575',
    database='ems'
)

mycursor=conn.cursor()

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('sample.html')

@app.route('/ADD')
def addemp():
    return render_template('add.html')

@app.route('/DELETE')
def deleteemp():
    return render_template('DELETE.html')

@app.route('/EDIT')
def editemp():
    return render_template('EDIT.html')

@app.route('/VIEW')
def viewemp():
    query='select * from employee'
    mycursor.execute(query)
    result=mycursor.fetchall()
    return render_template('VIEW.html',sqldata=result)

@app.route('/read', methods =['POST'])
def read():
    id = request.form['empid']
    name = request.form['empname']
    salary = request.form['empsal']
    dept = request.form['empdept']
    email = request.form['empemail']
    query = 'insert into employee values(%s, %s, %s, %s, %s)'
    data =(id, name, salary, dept,email)
    mycursor.execute(query,data)
    conn.commit()
    
    return render_template('add.html') 
@app.route('/delete', methods=['GET', 'POST']) 
def delete():
    if request.method == 'POST':
        empid = request.form['empid']
        query = "DELETE FROM employee WHERE emp_id=%s"
        data = (empid,)  
        mycursor.execute(query, data)
        conn.commit()

        return redirect(url_for('viewemp')) 

    return render_template('delete.html')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        empid = request.form['empid']
        name = request.form['empname']
        salary = request.form['empsal']
        dept = request.form['empdept']
        email = request.form['empemail']

        query = "UPDATE employee SET emp_name=%s, emp_salary=%s, emp_dept=%s, empemail=%s WHERE emp_id=%s"
        data = (name, salary, dept, email, empid)  
        mycursor.execute(query, data)
        conn.commit()
        return redirect(url_for('viewemp'))

    return render_template('EDIT.html')

if __name__ =='__main__':
    app.run(debug=True)