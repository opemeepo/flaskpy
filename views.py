from flask import Blueprint, jsonify, request
from flask_bcrypt import Bcrypt
import bcrypt

veiws_api = Blueprint('veiws_api', __name__)



users= []








@veiws_api.route('/signup', methods=['POST'])
def signup():
    
     
    if request.method == 'POST':
       req_data = request.get_json()

       user_id = req_data['user_id']
       password = user_id['password']
       hashed = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
       user_id['password'] = hashed
       users.append(user_id)

       return jsonify(user_id)
    else:
        return('signin here')

@veiws_api.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        req_data = request.get_json()
        email = users[0]['email']
        password = users[0]['password']
        #user_id = req_data['user_id']['email']
        #user_id2 = user_id['password']
        #resolve = {'email':user_id, 'password' : user_id2}
        return('welcome')
    else:
        return('login here')

@veiws_api.route('/user', methods=['GET'])
def user():
    return jsonify(users['password'])



    