from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template("index.html")


@app.route('/clickme', methods=['POST', 'GET'])
def clickMe():
    return render_template('index_troll.html')
