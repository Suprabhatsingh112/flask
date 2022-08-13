from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.form == 'POST' and request.form['username'] == 'admin':
        return redirect(url_for('success'))
    else:
        return redirect(url_for('index'))


@app.route('/success')
def success():
    return 'logged in successfully'


if __name__ == '__main__':
    app.run(debug=True)
