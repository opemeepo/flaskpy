from flask import Flask
from flask_bcrypt import Bcrypt
from flask import jsonify
from collections import defaultdict
from views import veiws_api
import bcrypt


app = Flask(__name__)
app.register_blueprint(veiws_api)
bcrypt = Bcrypt(app)

@app.route('/page')
def page():
    return jsonify('welcome')




if __name__ == '__main__':
    app.run()
