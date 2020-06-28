from flask import Flask

app = Flask(__name__)


@app.route('/signup')
def signup():
    return ('sign up here')

@app.route('/login')
def login():
    return ('login here')

if __name__ == '__main__':
    app.run()
