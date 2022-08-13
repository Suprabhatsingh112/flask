from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home1.html')


@app.route('/enternew')
def new_student():
    return render_template('student1.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            with sql.connect('database.db') as conn:
                cur = conn.cursor()
                cur.execute("insert into students (name,addr,city,pin) values(%s,%s,%s,%s)"(nm, addr, city, pin) )
                conn.commit()
                msg = "Record successfully added"
        except:
            conn.rollback()
            msg = "Error in insert operation"
        finally:
            return render_template("result1.html",msg=msg)
            conn.close()


@app.route('/list')
def list():
    conn=sql.connect('database.db')
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute('select * from students')
    rows=cur.fetchall()
    return render_template('list.html',rows=rows)


if __name__=="__main__":
    app.run(debug=True)



