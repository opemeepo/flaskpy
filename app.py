from flask import Flask, request, jsonify

app = Flask(__name__)


user = {}








@app.route('/signup', methods=['GET', 'POST'])
def signup():
    
     
    if request.method == 'POST':
       user = request.get_json()
       return ({'first_name':'ope',
'last_name':'oba', 
'email': 'lala',
'password': '2222',
'registeration_date' : '1/3/44'})
    else:
        return('signin here')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.get_json()
        return jsonify({"email" : "lacoste@yahoo.com", "password" : "jerusalema"}) 
    else:
        return('login here')


if __name__ == '__main__':
    app.run()
