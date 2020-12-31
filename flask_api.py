from flask import Flask, jsonify

app = Flask(__name__)

result = {'title': 'pythonTEST', 'result': 200}


@app.route('/test', methods=['GET', 'POST'])
def post_json():
    return jsonify(result)


if __name__ == "__main__":
    app.run(port=8081, debug=True)
