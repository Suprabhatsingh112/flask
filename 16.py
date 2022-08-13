from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)


class Students(db.Model):
    id = db.Column('students_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(200))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

    db.create_all()


@app.route('/')
def show_all():
    return render_template('show_all.html',Students=Students.query.all() )

@app.route('/new',methods=['GET','POST'])
def new():
    if request.method=='POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('please enter all the fields','error')
        else:
            student= Students(request.form['name'],
                              request.form['city'],
                              request.form['addr'],
                              request.form['pin'])

            db.session.add(student)
            db.session.commit()
            flash ('record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')


