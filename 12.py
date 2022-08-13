from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'singhsuprabhat7@gmail.com'
app.config['MAIL_PASSWORD'] = '6206086329@bittu'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def index():
    msg = Message('hello', sender='singhsuprabhat7@gmail.com', recipients=['singhsuprabhat007@gmail.com'])
    msg.body = 'hello flask this message is sent from flask mail'
    mail.send(msg)
    return 'message sent'


if __name__ == '__mail__':
    app.run(debug=True)
