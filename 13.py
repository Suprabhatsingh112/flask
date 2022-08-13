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
