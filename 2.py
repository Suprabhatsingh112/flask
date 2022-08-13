from flask import Flask, redirect, url_for
"""" different method of routing"""
app = Flask(__name__)

@app.route('/')
def hello():
    return f'hello world '

@app.route('/admin')
def hello_admin():
    return f'Hello admin, this is the admin page'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return f'hello {guest},this is the guest page'

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


if __name__ == '__main__':
    app.run(debug=True)
