from flask import Flask, request
import requests
import json
import data as D
import model as M
import csv

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    '''
    RESTful API that reads input data from a JSON data in HTTP POST.
    '''
    data = request.data.decode('utf-8')
    data = json.loads(data)
    # YOUR CODE HERE - Preprocess]

    value = []
    for i in data:
        value.append(D.preprocess(i))

    output = []
    for i in value:
        output.append(int(M.predict(i)))

    # YOUR CODE HERE - Return a JSON format
    count = 0
    for i in data:
        i['target'] = output[count]
        count = count + 1
    return {"data": json.dumps(data)}


@app.route('/')
def index():
    '''Start page for testing.'''
    return 'Welcome to Website'


@app.route('/sample', methods=['GET'])
def sample():
    '''
    RESTful API used to test the prediction API by simulating one sample, 
    package such sample in a JSON file, and send a HTTP POST to the prediction API.
    '''
    # YOUR CODE HERE - Sample data
    payload = []

    readfile = []
    with open('hw1_std.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            readfile.append(row)

    for i in readfile[1:]:
        ai = {}
        count = 1
        for j in i[1:]:
            if j is '':
                ai[readfile[0][count]] = 0
            else:
                try:
                    ai[readfile[0][count]] = int(j)
                except TypeError:
                    ai[readfile[0][count]] = float(j)
                except:
                    ai[readfile[0][count]] = j
            count = count + 1
        payload.append(ai)
    # Send a HTTP POST to the prediction API
    r = requests.post(
        'http://localhost:5000/predict', data=json.dumps(payload)
    )
    res = r.json()
    print("awdawd", res['data'])
    return res['data']


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
