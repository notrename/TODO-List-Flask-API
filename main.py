from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/todo/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': {}})


if __name__ == '__main__':
    app.run(debug=True)