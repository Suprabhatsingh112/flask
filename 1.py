from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'


@app.route('/hello/<name>')
def hello_name(name):
    return f'hello {name}'


if __name__ == '__main__':
    app.run(debug=True)
