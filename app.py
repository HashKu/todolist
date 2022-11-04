from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<html><body style="color: Red">Hello, Web!<body></html>'

@app.route('/bye')
def bye():
    return 'Bye'

app.run(debug=True)