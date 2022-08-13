from flask import Flask, redirect, render_template, url_for, request, flash

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'invalid username or password please try again'
        else:
            flash('you are successfully logged in')
            flash('logout before login again')
            return redirect(url_for('index'))
    return render_template('log_in.html', error=error)

app.secret_key='jkjkllllonh'
if __name__ == '__main__':
    app.run(debug=True)
