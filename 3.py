from flask import Flask, redirect, request, url_for

app = Flask(__name__)


@app.route('/welcome/<name>')
def welcome(name):
    return f'welcome you {name}'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('welcome', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('welcome', name=user))


if __name__ == '__main__':
    app.run(debug=True)


