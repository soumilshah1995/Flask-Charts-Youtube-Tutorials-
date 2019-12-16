from flask import Flask,render_template,url_for,request,redirect
import json, random

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/temperature', methods=["GET", "POST"])
def temperature():
    temperature = []
    for i in range(1,10):
        temperature.append(random.randint(0,100))
    data = {
        "temperature":temperature
    }
    return data


if __name__ == "__main__":
    app.run(debug=True)
