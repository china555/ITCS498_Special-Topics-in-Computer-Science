from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return'Mahidol'


@app.route('/itcs498', methods=['POST', 'GET'])
def fucntion2():
    return 'itcs498'


if __name__ == '__main__':
    app.run(debug=True)
