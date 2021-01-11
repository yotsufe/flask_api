from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/test', methods=['GET', 'POST'])
def return_result():
    return jsonify(result)


result = {'title': 'pythonTEST', 'result': 200}


@app.route('/user', methods=['GET', 'POST'])
def return_user():
    return jsonify(user_json)


user_json = {'id': 1, 'name': "Michel", "password": "asdf"}


@app.route('/users', methods=['GET', 'POST'])
def return_users():
    return jsonify(users_json)


users_json = {
    "users": [
        {'id': 1, 'name': "Michel", "password": "asdf"},
        {'id': 2, 'name': "Bob",    "password": "qwer"},
        {'id': 3, 'name': "Jack",   "password": "zxcv"}
    ]
}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)
