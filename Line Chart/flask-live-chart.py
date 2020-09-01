import json
from time import time
from random import random
from flask import Flask, render_template, make_response
import requests



app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/live-data')
def live_data():

    # API CALL HERE
    # url = ""
    # data = requests.get(url)
    # data = data.json()
    # # DATA SHOULD BE ARRAY

    x =  [time() * 1000,time() * 1000,time() * 1000,time() * 1000,time() * 1000]
    y = [1,2,3,4,5,7,8,9,10]
    data = [x,y]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
