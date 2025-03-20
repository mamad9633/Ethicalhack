from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data['username'] == 'admin' and data['password'] == 'admin':
        return {'message': 'Login successful'}
    return {'message': 'Invalid credentials'}, 401

if __name__ == '__main__':
    app.run(debug=True)
