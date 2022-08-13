from flask import Flask, render_template,request,flash

app=Flask(__name__)
app.secret_key='epeelel'

from flask_wtf import Form
from wtforms import  IntegerField,TextAreaField, SubmitField, RadioField,SelectField

from wtforms import validators

class ContactForm(Form):
    name=TextAreaField('name of student',[validators.DataRequired('please enter your name')])
    Gender= RadioField('Gender',choices=[('M','MALE'),('F','FEMALE')])
    Address=TextAreaField('Address')

    email = TextAreaField('Email',[validators.DataRequired('please enter your email address.'),validators.Email('please enter your email ')])

    Age= IntegerField('age')
    language=SelectField('Language',choices=[('cpp', 'c++'),('py','python')])
    submit=SubmitField('send')

@app.route('/contacts', methods=['GET','POST'])
def contact():
    form=ContactForm()

    if request.method=='POST':
        if not form.validate():
            flash('all fields required.')
            return render_template('contact.html',form=form)
        else:
            return render_template('success.html')
    if request.method=='GET':
        return render_template('contact.html',form=form)


if __name__=='__main__':
    app.run(debug=True)
